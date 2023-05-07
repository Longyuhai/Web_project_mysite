from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class People(models.Model):
    name=models.CharField(null=True,blank=True,max_length=200)
    sex=models.CharField(null=True,blank=True,max_length=2)

class Article(models.Model):
    """docstring forArticle."""
    headline=models.CharField(null=True,blank=True,max_length=100)
    content=models.CharField(null=True,blank=True,max_length=10000)
    TAG_CHOICES=(
    ('科技','tech'),
    ('生活','life'),
    )
    tag=models.CharField(null=True,blank=True,max_length=50,choices=TAG_CHOICES)
    def __str__(self):
        return self.headline

class Comment(models.Model):
    name=models.CharField(null=True,blank=True,max_length=50)
    comment=models.TextField(null=True,blank=True)
    article_to=models.ForeignKey(to=Article,related_name='article_comments',on_delete=models.CASCADE,
    null=True,blank=True)
    def __str__(self):
        return self.comment

class UserProfile(models.Model):
    belong_to=models.OneToOneField(to=User,related_name='profile',on_delete=models.CASCADE)
    profile_image=models.FileField(upload_to='imgs')
    def __str__ (self):
        return self.belong_to.username

class Ticket(models.Model):
    voter=models.Foreignkey(to=UserProfile,related_name='voted_tickets',on_delete=models.CASCADE)
    article=models.Foreignkey(to=Article,related_name='tickets',on_delete=models.CASCADE)
    VOTE_CHOICES=(
    ('喜欢','like'),
    ('不喜欢','dislike'),
    ('未投票','normal'),
    )
    choice=models.CharField(choice=VOTE_CHOICES,max_length=10)
    def __str__(self):
        return str(self.id)
