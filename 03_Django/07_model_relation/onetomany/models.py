from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=20)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'

    # 2번 댓글을 쓴 사람의 모든 게시글?
    # 1번 글의 첫번째 댓글/ 마지막 댓글 사람의 이름
    # 1번글의 두번째 ~ 네번째 댓글
    # 1번글의 첫번째 ~ 두번째 댓글
    # 1번글의 2번째 댓글작성자의 첫번째 게시물의 작성자 이름
    # 1번댓글의 유저정보만

    # 1번 댓글의 user 정보만 가져오면? Comment.objects.all().values('user')
    # 2번 사람이 작성한 댓글을 content를 기준으로 내림차순으로 가져오면?
    # 제목이 '1글'인 게시글은?