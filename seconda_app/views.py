from django.shortcuts import render
import datetime

# Create your views here.

def esempio_if(request):
    dic = { 'var1': 200,
    'var2': 200,
    'var3': 300 }
    return render(request, "es_if.html", dic)

def if_else_elif(request):
    dic = { 'var1': 200,
    'var2': 200,
    'var3': 300 }
    return render(request, "if_else_elif.html", dic)

def es_for(request):
    dic = { 'list1': [1, datetime.date(2019,7,16), 'Do not give up!'], 'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] } 
    return render(request, "es_for.html", dic)