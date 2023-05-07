from django.shortcuts import render,redirect
from myapp.models import People
from django.template import Context,Template
from django.http import HttpResponse
from myapp.models import Article,Comment
from myapp.form import CommentForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login
from myapp.form import LoginForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.
def first_page(request):
    person=People(name='陆羽',sex='女')
    htmlstring="<html><head><title></title></head><body>hello,{{ person.name}}</body></html>"
    t=Template(htmlstring)
    c=Context({'person':person})
    web=t.render(c)
    return HttpResponse(web)

def index(request):
    context={}
    q=request.GET.get('tag')
    if q:
        article_list=Article.objects.filter(tag=q)
    else:
        article_list=Article.objects.all()
    p=Paginator(article_list,3)
    page_n=request.GET.get('page')
    try:
        article_list=p.page(page_n)
    except EmptyPage:
        article_list=p.page(p.num_pages)
    except PageNotAnInteger:
        article_list=p.page(1)
    context['article_list']=article_list
    index_page=render(request,'index.html',context)
    return HttpResponse(index_page)

def detail(request,page_num):
    if request.method=='GET':
        form=CommentForm
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            comment=form.cleaned_data['comment']
            a=Article.objects.get(id=page_num)
            c=Comment(name=name,comment=comment,article_to=a)
            c.save()
            return redirect(to='detail',page_num=page_num)
    context={}
    # comment_list=Comment.objects.all()
    article=Article.objects.get(id=page_num)
    context['article']=article
    # context['comment_list']=comment_list
    context['form']=form
    return render(request,'article_detail.html',context)

def index_login(request):
    context={}
    if request.method=='GET':
        form=AuthenticationForm
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #username=form.cleaned_data['username']
            #password=form.cleaned_data['password']
            #user=authenticate(username=username,password=password)
            #if user:
            #    login(request,user)
            #    return redirect(to='index')
            login(request,form.get_user())
            return redirect(to='index')
        else:
            return HttpResponse('<h1>用户登录密码错误！</h1>')
    context['form']=form
    return render(request,'login.html',context)

def index_register(request):
    context={}
    if request.method=='GET':
        form=UserCreationForm
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form']=form
    return render(request,'login.html',context)
