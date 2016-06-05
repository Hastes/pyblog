import datetime
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context
from django.template.loader import get_template
from django.utils import timezone

#from pyt1.post_habr import GetContentHabr, GetTitleHabr
from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()[:5]
    return render(request, 'index2.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
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

###def PostHabr(request):
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