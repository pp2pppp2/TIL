# Django

python -m venv venv 가상환경 설정

source venv/Scripts/activate

pip install django

django-admin startproject classroom .

python manage.py startapp home



project -- settings  -> INSTALLED_APPS  app의 이름을 추가.



django Built-in template tags and filters



{% csrf_token %}



LANGUAGE_CODE = 'ko-kr'



TIME_ZONE = 'Asia/Seoul'



## db

models.py 수정 (table 정리.)

python manage.py makemigrations

python manage.py migrate



python manage.py shell



class.objects.all()

class.save()



class.objects.create()

class.objects.filter()

.first()

.last()

.get() 겹치면 Error



class.objects.order_by('id') or ('-id')

filter(title__contains='??')

filter(title__startswith='first')

endswith





admin.site.register(Article)



## CRUD

Create

Read

Update

Delete