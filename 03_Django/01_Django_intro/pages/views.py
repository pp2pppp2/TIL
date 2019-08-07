from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def introduce(request, name):
    student ={
        '김길동' : 21,
        '홍길동' : 20,
        '박길동' : 28,
    }
    context = {
        'name' : name,
        'age' : student.get(name),
    }
    return render(request, 'pages/introduce.html', context)

def image(request):
    return render(request, 'pages/image.html')

# Template Variable 템플릿 변수
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '어쩌구']
    pick = random.choice(menu)
    context = {'pick': pick }
    return render(request, 'pages/dinner.html', context )

# Variable Routing (동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '어쩌구']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age,
        'pick': pick, 
    }
    return render(request, 'pages/hello.html', context )

# 실습
# 1. 동적 라우팅을 활용하여 name 과 age 를 인자로 받아, 자기소개 페이지
def introself(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request,'pages/introself.html', context )

# 2. 두개의 숫자를 인자로 받아 (num1 , num2) 곱셈결과를 출력.
def mul(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request,'pages/mul.html', context)

# r 을 받아 널빙 구하시오

def circle(request, r):
    pi = 3.14
    result = pi * r **2
    context = {
        'result':result
    }
    return render(request, 'pages/circle.html', context)

# DTL
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus' : menus,
        'my_sentence' : my_sentence,
        'messages' : messages,
        'empty_list' : empty_list,
        'datetimenow' : datetimenow,
    }

    return render(request, 'pages/template_language.html', context )

# 실습 1
# isbirth

def isbirth(request):
    today = datetime.now()
    days = today.day
    months = today.month
    result = "아니오"
    if days == 26 and months ==11:
        result = "예"
    context = {
        'result' : result,
        'days' : days,
        'months' : months,
    }
    return render(request, 'pages/isbirth.html', context )

#회문판별
def ispal(request, word):
    result = "회문입니다."
    for idx, wd in enumerate(word):
        if not word[idx] == word[len(word)-idx-1]:
            result ="아닙니다."
    context = {
        'result' : result,
    }
    return render(request, 'pages/ispal.html', context )

#lotto 로또 번호 추첨
#lottos -> 1~45 까지 번호중 6개를 랜덤으로 pick
#real_lottos -> [21, 24, 30, 32, 40, 42]
#lottos 번호를 DTL 활용해 출력
#컴식이가 뽑은 번호와 실제 번호 비교 DTL if

def lotto(request):
    lotto = random.sample(range(1,46), 6)
    real_lottos = [21, 24, 30, 32, 40, 42]
    cnt = 0
    context = {
        'lotto' : lotto,
        'real_lottos' : real_lottos,
        'cnt' : cnt,
    }
    return render(request, 'pages/lotto.html', context )

# Form - GeT

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message' : message,
        'message2' : message2,
    }
    return render(request, 'pages/catch.html', context )

def ping(request):
    text = request.GET.get('text')
    context = {
        'text' : text,
    }
    return render(request, 'pages/ping.html', context)

def pong(request):
    text2 = request.GET.get('text2')
    context = {
        'text2' : text2,
    }
    return render(request, 'pages/pong.html', context)
    
#8 form get 실습 ascii art

def art(request):
    return render(request, 'pages/art.html')

def result(request):
    word = request.GET.get('word')
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    fonts = fonts.split('\n')
    font = random.choice(fonts)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context = {
        'result' : result,
    }
    return render(request, 'pages/result.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name' : name,
        'pwd' : pwd,
    }
    return render(request, 'pages/user_create.html', context )

#10 정적파일

def static_example(request):
    return render(request, 'pages/static_example.html')