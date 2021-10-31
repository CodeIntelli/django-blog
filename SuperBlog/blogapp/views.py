from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
# Create your views here.


def home(request):
    # load all the post from database(10)
    post_Data = Post.objects.all()[:11]
    print(post_Data)
    cats = Category.objects.all()
    # data = {
    #     'post_Data': post_Data
    #     'cats': cats
    # }
    return render(request, 'index.html',  {
        'post_Data': post_Data,
        'cats': cats
    })


def post(request, url):
    postData = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {"postData": postData, 'cats': cats})


def categories(request, url):
    cat = Category.objects.get(url=url)
    print(cat)
    posts = Post.objects.filter(cat=cat)
    print(posts)
    cats = Category.objects.all()
    data = {
        'cat': cat,
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'category.html', data)
