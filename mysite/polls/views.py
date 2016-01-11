from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

from django.template import loader

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	# output=','.join([q.question_text for q in latest_question_list])
	template=loader.get_template('polls/index.html')
	context={
	'latest_question_list':latest_question_list
	}
	return render(request,'polls/index.html',context)

def results(request,question_id):
	response='Your are looking at the results of question %s'
	return HttpResponse(response%question_id)

def vote(request,question_id):
	return HttpResponse('Your are voting on quesiton %s.'%question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
