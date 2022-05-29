from django.shortcuts import redirect,render
from .models import *
from django.http import HttpResponse
 
# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=AddQuiz.objects.all()
        score=100
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                correct+=1
            else:
                score-=20
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=AddQuiz.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)