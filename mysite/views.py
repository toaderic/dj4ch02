from django.shortcuts import render , redirect
from mysite.models import Post
from datetime import datetime

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request , 'index.html' , locals())

def showpost(request , slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request , 'post.html' , locals())
    except:
        return redirect('/')


    # for count , post in enumerate(Posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
    #     post_lists.append("<small>" + str(post.body) + "</small><br><br>")
    # return HttpResponse(post_lists)


# Create your views here.
