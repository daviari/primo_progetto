from django.shortcuts import render
from random import randint, random
import datetime

# Create your views here.
def somma(request):
    dic = { 'var1': randint(1,10),
    'var2': randint(1,10) }
    return render(request, "somma.html", dic)

def media(request):
    dic = { 'var1': randint(1,10),
    'var2': randint(1,10),
    'var3': randint(1,10),
    'var4': randint(1,10),
    'var5': randint(1,10),
    'var6': randint(1,10),
    'var7': randint(1,10),
    'var8': randint(1,10),
    'var9': randint(1,10),
    'var10': randint(1,10),
    'var11': randint(1,10),
    'var12': randint(1,10),
    'var13': randint(1,10),
    'var14': randint(1,10),
    'var15': randint(1,10),
    'var16': randint(1,10),
    'var17': randint(1,10),
    'var18': randint(1,10),
    'var19': randint(1,10),
    'var20': randint(1,10),
    'var21': randint(1,10),
    'var22': randint(1,10),
    'var23': randint(1,10),
    'var24': randint(1,10),
    'var25': randint(1,10),
    'var26': randint(1,10),
    'var27': randint(1,10),
    'var28': randint(1,10),
    'var29': randint(1,10),
    'var30': randint(1,10) }
    return render(request, "media.html", dic)

def voti(request):
    
    dic = { 'studente1': [1, datetime.date(2019,7,16), 'Voto:'], 'studente2': [2, datetime.date(2019,7,16), 'voto'] } 
    return render(request, "voti.html", dic)
