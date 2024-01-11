from django.shortcuts import render, get_object_or_404
from . models import Post as Blog
from . models import Category
# Create your views here.
# def blog(request):
#     return render(request, "blog/blog.html")

def blog(request):
    blog = Blog.objects.all()
    # category = Category.objects.all('name')
    return render(request, "blog/blog.html", {'blogs':blog})


def category(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    return render(request,"blog/category.html",{'category':category})
    