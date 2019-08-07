from django.urls import path
from . import views

urlpatterns = [
    path('static_exaple/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('ispal/<str:word>/', views.ispal),
    path('lotto/', views.lotto),
    path('isbirth/', views.isbirth),
    path('template_language/', views.template_language),
    path('circle/<int:r>/', views.circle),
    path('mul/<int:num1>/<int:num2>/', views.mul),
    path('introself/<str:name>/<int:age>/', views.introself),
    path('hello/<str:name>/<int:age>/', views.hello),
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('introduce/<str:name>/', views.introduce),
    path('index/', views.index),
]