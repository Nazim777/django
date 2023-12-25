from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from service.models import BlogPost

def Home(request):
    data = {
        "page":"Home page"
    }
    return render(request,"index.html",data)
def aboutUs(request):
    data = {
        "page":"about page",
        "fruits":['banana','orange','jack fruit'],
        "users":[
            {'name':"rahim","email":"rahim@gmail.com"},
            {"name":"habib","email":"habib@gmail.com"}
        ],
        "numbers":[20,30,40,50,60]
    }
    return render(request,"about.html",data)

def blog(request):
    blog_posts = BlogPost.objects.all()
    items_per_page = 2
    paginator = Paginator(blog_posts, items_per_page)
    page = request.GET.get('page')
    try:
        # Get the Page object for the requested page
        all_blog_obj = paginator.page(page)
    except PageNotAnInteger:
         # If page is not an integer, deliver the first page
        all_blog_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results
        all_blog_obj = paginator.page(paginator.num_pages)   
    if request.method=="GET":
        if request.GET.get('blog_title') == "":
            return render(request,'blog.html',{"error":True,'msg':"search field is required!",'blog_posts': all_blog_obj})
        bt = request.GET.get('blog_title')
        if bt !=None:
           all_blog_obj = BlogPost.objects.filter(title__icontains=bt)
    return render(request,'blog.html', {'blog_posts': all_blog_obj})

def blogDetails(request,id):
    blog_post = get_object_or_404(BlogPost, pk=id)
    return render(request,'blogDetails.html',{'blog_post': blog_post})

def contact(request):
    users={}
    try:
        if request.method=="POST":
            if request.POST['name'] =="":
                return render(request,'contact.html',{"error":True,'msg':"name field is required!"})
            
            if request.POST['email'] =="":
                return render(request,'contact.html',{"error":True,'msg':"email field is required!"})
               
            name = request.POST['name']
            email = request.POST['email']
            users={
                'name':name,
                'email':email
            }
            url = '/userinfo/?info={}'.format(users)
            return redirect(url)
            # return HttpResponseRedirect(url)
        
        
    except:
        pass    
    return render(request,'contact.html')


def userinfo(request):
    if request.method=="GET":
        users={}
        info = request.GET.get('info')
        if info:
          users = eval(info)
    return render(request,'userinfo.html',users)