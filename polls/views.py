from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404

# Create your views here.


class IndexView(generic.ListView):
    """ Index view for the polls app.

    Methods:
        get_queryset(): Returns the last five published question.
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Returns the last five published questions (excluding those set to be published in the future).

        Returns:
            QuerySet: A queryset containing the latest published questions.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """ Detail view for the polls app. """
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        question = get_object_or_404(Question, pk=kwargs['pk'])
        if question.can_vote():
            return render(request, 'polls/detail.html', {'question': question})
        else:
            raise Http404


class ResultsView(generic.DetailView):
    """ Results view for the polls app. """
    model = Question
    template_name = 'polls/results.html'

    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        question = get_object_or_404(Question, pk=kwargs['pk'])
        total_votes = sum([choice.votes for choice in question.choice_set.all()])
        if question.can_vote():
            return render(request, 'polls/results.html', {'question': question, 'total_votes': total_votes})
        else:
            raise Http404


def index(request: HttpRequest) -> HttpResponse:
    """ Index view for the polls app.

    Returns:
        HttpResponse: A HttpResponse object containing the rendered index.html.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    """ Detail view for the polls app.

    Args:
        request (HttpRequest): Object that contains metadata about the request.
        question_id (int): The id of the question.

    Returns:
        HttpResponse: A HttpResponse object containing the rendered detail.html.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    """ Results view for the polls app.

    Args:
        request (HttpRequest): Object that contains metadata about the request.
        question_id (int): The id of the question.

    Returns:
        HttpResponse: A HttpResponse object containing the rendered results.html.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    """ Vote view for the polls app.
    Args:
        request (HttpRequest): Object that contains metadata about the request.
        question_id (int): The id of the question.

    Returns:
        HttpResponse: A HttpResponse object containing the rendered results.html.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
