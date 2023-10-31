from django.shortcuts import render , HttpResponse , redirect
from blog.models import Post , blogcomment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    context = {'allposts':allpost}
    return render(request,'blog/bloghome.html',context)
    

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first() 
    post.views = post.views + 1
    post.save()
    comments = blogcomment.objects.filter(post = post , parent = None)
    replies = blogcomment.objects.filter(post = post).exclude(parent=None)
    repdict = {}
    for reply in replies:
        if reply.parent.sno not in repdict.keys():
            repdict[reply.parent.sno] = [reply]
        else:
            repdict[reply.parent.sno].append(reply)
    # print(repdict)
    context = {'post':post , 'comments':comments,'user':request.user , 'repdict':repdict}
    return render(request,'blog/blogpost.html', context)
    

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("postsno")
        post = Post.objects.get(sno = postsno)
        parentsno = request.POST.get("parentsno")
        if parentsno == "":
            comment = blogcomment(comment = comment ,user = user , post = post)
            comment.save()
            messages.success(request , "Your comment  has been posted successfully")
        else:
            parent = blogcomment.objects.get(sno=parentsno)
            comment = blogcomment(comment = comment ,user = user , post = post , parent=parent)
            comment.save()
            messages.success(request , "Your reply  has been posted successfully")

    return redirect(f"/blog/{post.slug}")
    