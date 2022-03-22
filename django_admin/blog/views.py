from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


posts =[
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 27,2018',
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'August 28,2018',
    }
]
def home(request):
    context ={
        'posts':posts
    }
    # return HttpResponse('<h1>blog home</h1>')
    return render(request,'blog/home.html',context)

# Create your views here.

def about(request):
    # return HttpResponse('<h1>blog about</h1>')
    return render(request,'blog/about.html',{'title':'About'})