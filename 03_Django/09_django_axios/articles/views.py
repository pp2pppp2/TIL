from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.http import JsonResponse, HttpResponseBadRequest
import hashlib


def index(request):
    #1. session 정보에서 visits_num 이라는 키로 접근해 값을 가져옴
    # 해당하는 키가 없으면 0을 가져옴.
    visits_num = request.session.get('visits_num', 0)

    #2. 가져온 값을 session에 'visits_num' 이라는 새로운 키의 값으로 1씩 증가
    request.session['visits_num'] = visits_num + 1

    #3. session data를 수정하면 Django는 수정한 내용을 알 수 없어서 작성하는 거
    request.session.modified = True

    articles = Article.objects.all()
    context = { 'articles': articles, 'visits_num':visits_num, }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    """
    Form class:
    모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 데이터 정제
    후 DB에 저장 하는 실제 로직이 필요

    Model Form:
    이미 Model에 대한 정보를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고 있음
    form.save() 만 해도 DB에 저장됨
    """

    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid(): 
            # form.cleaned_data 를 통해 폼 데이터를 정제한다 ( form.cleaned_data => DICT )
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            # embed()
            article=form.save(commit=False)
            article.user_id = request.user.pk
            article.save()
            # 1 content를 공백 기준으로 리스트로 변경 후 for문
            for word in article.content.split():
                # 2 #으로 시작하는 요소 선택
                if word.startswith('#'):
                    # 3.word랑 같은 해시태그 찾고 없으면 새로운 객체
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # 4. 게시글의 해시태그 목록에 해당 단어를 추가
                    article.hashtags.add(hashtag)
                    
            # embed()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {'form': form, }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = article.comments.all()
    person = get_object_or_404(get_user_model(), pk=article.user.pk)
    comment_form = CommentForm()
    # article = Article.objects.get(pk=article_pk)
    context = {'article':article, 'comments' : comment, 'comment_form':comment_form, 'person':person, }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.user != request.user:
        return redirect('articles:index')
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk) # 주석가능이요.
        # if request.method == "POST":
        # if article.user == request.user:
        article.delete()
    return redirect('articles:index')
    # return redirect('articles:detail', article.pk)

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.user != request.user:
        return redirect('articles:index')
    if request.method == 'POST':
        # instance -> 수정의 대상이 되는 특정한 글 객체
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            article = form.save()
            article.hashtags.clear()
            for word in article.content.split():
                if word.startswith('#'):
                    hashtag, created = Article.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)
        return redirect('articles:detail', article.pk)
    else:
        # form = ArticleForm(initial={
        #     'title': article.title,
        #     'content': article.content,
        # })
        # form = ArticleForm(initial=article.__dict__)
        form = ArticleForm(instance=article)
    context = {'form': form, }
    return render(request, 'articles/form.html', context)

"""
Create Logic
1.GET
- 사용자가 데이터를 입력할 수 있는 빈 Form 제공
There's a blank form for user to input the data.
2.POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update Logic
1.GET
-기존 사용자의 글이 입력된 Form 제공
2.POST
-수정된 글을 DB에 저장
"""


@require_POST
def comment_create(request, article_pk):
    # if request.method == 'POST':
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user_id = request.user.pk
            comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        # if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)


@login_required
def comment_update(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = article.comments.all()
    comment_form = CommentForm()
    comment_updated = Comment.objects.get(pk=comment_pk)
    if comment_updated.user != request.user:
        return redirect('articles:index')
    comment_form_update = CommentForm(instance=comment_updated)
    isupdate = 0
    if request.method == 'POST':
        comment_form_update = CommentForm(request.POST ,instance=comment_updated)
        if comment_form_update.is_valid():
            comment_form_update.save()
            isupdate = 1
    context = {
        'article':article,
        'comments' : comment, 
        'comment_form':comment_form,
        'comment_form_update':comment_form_update,
        'comment_updated' : comment_updated,
        'isupdate' : isupdate ,
        }
    return render(request, 'articles/detail.html', context)

@login_required
def like(request, article_pk):
    if request.is_ajax():
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user
        
        # 해당 게시글에 좋아요를 누른 사람들 중에서 user.pk(현재 요청 유저)를 가진 user가 존재하면
        if article.like_users.filter(pk=user.pk).exists():
            # 좋아요 취소
            article.like_users.remove(user)
            liked = False
        else:
            # 좋아요 누름
            article.like_users.add(user)
            liked = True
        count = article.like_users.count()
        context = { 'liked':liked, 'count':count, }
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()

@login_required
def follow(request, article_pk, user_pk):
    # 게시글을 작성한 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 해당 함수로 요청을 보낸 사람
    user = request.user
    
    # 해당 person 의 followers 중에서 해당유저가 존재하면
    if person.followers.filter(pk=user.pk).exists():
        # unFollow
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('articles:detail', article_pk)

@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.articles.order_by('-pk')
    context = {'hashtag':hashtag, 'articles':articles, }
    return render(request, 'articles/hashtag.html', context )