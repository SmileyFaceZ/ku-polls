from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from polls.models import Question, Choice, Vote
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class IndexView(generic.ListView):
    """ Index view for the polls app.

    Methods:
        get_queryset(): Returns the last five published question.
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Returns the last five published questions
        (excluding those set to be published in the future).

        Returns:
            QuerySet: A queryset containing the latest published questions.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())\
            .order_by('-pub_date')


class DetailView(LoginRequiredMixin, generic.DetailView):
    """ Detail view for the polls app.
    Methods:
        get_queryset(): Returns the question is less than or
        equal to the current time.
        get(): Returns the detail view for a given question.
    """
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:

        this_user = request.user

        try:
            question = get_object_or_404(Question, pk=kwargs["pk"])
        except Http404:
            messages.error(
                request,
                f"Question number {kwargs['pk']} does not exists.❗️")
            return redirect("polls:index")

        try:
            vote = Vote.objects.get(user=this_user, choice__question=question)
            selected_choice = vote.choice
            has_voted = True
        except Vote.DoesNotExist:
            has_voted = False
            selected_choice = None

        context = {
            'question': question,
            'has_voted': has_voted,
            'choice_text': selected_choice,
            'selected_choice': selected_choice,
        }

        if has_voted or question.can_vote():
            return render(request, 'polls/detail.html', context)
        else:
            raise Http404


class ResultsView(generic.DetailView):
    """ Results view for the polls app.

    Methods:
        get(): Returns the results for a given question.
    """
    model = Question
    template_name = 'polls/results.html'

    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        try:
            question = get_object_or_404(Question, pk=kwargs["pk"])
        except Http404:
            messages.error(
                request,
                f"Result question number {kwargs['pk']} does not exists.❗️")
            return redirect("polls:index")

        total_votes = \
            sum([choice.votes for choice in question.choice_set.all()])
        context = {'question': question, 'total_votes': total_votes}
        return render(request, 'polls/results.html', context)


@login_required
def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    """ Vote view for the polls app. """
    question = get_object_or_404(Question, pk=question_id)
    this_user = request.user

    if not this_user.is_authenticated:
        return redirect('login')

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.❗",
        })

    try:
        vote = Vote.objects.get(user=this_user, choice__question=question)
        vote.choice = selected_choice
        question_objects = Question.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')
        vote.save()
        return render(request, 'polls/index.html',
                      {'message': '⭐️ Vote successfully updated ⭐️️',
                       'latest_question_list': question_objects,
                       'choice_id': question_id})

    except Vote.DoesNotExist:
        vote = Vote.objects.create(user=this_user, choice=selected_choice)
        vote.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def signup(request) -> HttpResponse:
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)

        return redirect('polls:index')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
