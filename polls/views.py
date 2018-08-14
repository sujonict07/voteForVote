from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader
from .models import Question


def index(requset):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # output = ', '.join(q.question_text for q in latest_question_list)
    # return HttpResponse(template.render(context, requset))
    return render(requset, 'polls/index.html',context)


def details(request, question_id):
    # return HttpResponse("You are looking at Question no {}".format(question_id))
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.doesNotExist:
    #     raise Http404("Question does not exists.")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question':question})



def results(request, question_id):
    return HttpResponse("You are looking results at Question no {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("You are voting at Question no {}".format(question_id))



