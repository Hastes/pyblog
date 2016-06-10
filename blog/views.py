#import datetime
#from django.contrib import admin
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect,  render_to_response
#from django.template import Context
#from django.template.loader import get_template
from django.utils import timezone
from django.core.context_processors import csrf

#from pyt1.post_habr import GetContentHabr, GetTitleHabr
from .forms import PostForm,CommentForm
from .models import Post,Comment

#from django.template import loader,Context


def post_list(request):
    args={}
    vievlogin = str(request.user)
    if (vievlogin == "hastes"):
        args['adminpanel']= True
    args['user']=vievlogin
    args['posts'] = Post.objects.all()[:5]
    return render(request, 'post_list.html', args)
def post_detail(request, pk):
    title = Post.objects.all()[:5]
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post,'posts':title})
def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'post_edit.html', {'form': form})
def chat(request):

    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['form']=comment_form
    comment_list= Comment.objects.all()[:10]
    args['comments']=comment_list
    return render(request,'chat_list.html',args)

def addlike(request,com_id):
    if com_id in request.COOKIES:
        return redirect('/chat/')
    else:
        com=get_object_or_404(Comment,id=com_id)
        com.likes+=1
        com.save()
        response =redirect('/chat/')
        response.set_cookie(com_id,"test")
        return response

def addcomment(request):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
    return redirect('/chat/')
def about(request):
    return render(request,'about2.html')


##def PostHabr(request):
  #  post = Post.objects.filter(published_date__lte=timezone.now())[0]
   # oldtitle = post.title
  #  newtitle= GetTitleHabr()
  #  print(oldtitle, newtitle)
  #  if oldtitle != newtitle:
  #      title = GetTitleHabr()
   #     oldtitle=title
  #      Post.objects.create(author=request.user, title=title, text=GetContentHabr(),published_date = timezone.now())
   #     return HttpResponseRedirect("http://localhost:8000/")
  #  else:
 #       return HttpResponse("Post usje dobavlen")