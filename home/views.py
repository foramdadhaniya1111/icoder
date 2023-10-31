from django.shortcuts import render , HttpResponse , redirect
from .models import contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
# HTML pages
def home(request):
    return render(request,'home/home.html')

def about(request):
     return render(request,'home/about.html')

def contact1(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name , email , phone , content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request , "Please fill the form currectly")
        else:
            ins=contact(name=name,email=email,phone=phone,content=content)
            ins.save()
            messages.success(request, "Your message has been send")

    return render(request,'home/contact.html')
   
def search(request):
    query =request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none() 
    else:
        allpoststitle =Post.objects.filter(title__icontains=query)
        allpostscontent = Post.objects.filter(content__icontains=query)
        allposts = allpoststitle.union(allpostscontent)
    if allposts.count() == 0:
        messages.warning (request , "No Search results found.Please refine your query ")
    params={'allposts':allposts , 'query':query}
    return render(request,'home/search.html' , params )


#Authenticated APIS
def handlesignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #checks for errorneous inputs
        # username should be 10 charactor

        if len(username)> 10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('home')
        
        # username shoud be alphanumeric
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect('home')
        
        # both password must be same
        if pass1 != pass2:
            messages.error(request , "password do not match")
            return redirect('home')
        
    

        #createt the user
        myuser = User.objects.create_user(username , email , pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request ,  "Your icoder Accounr has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 - not Found")

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username =loginusername ,password = loginpassword)

        if user is not None:
            login(request , user)
            messages.success(request , "successfully logged In")
            return redirect('home')
        else:
            messages.error(request , "Invalid username or password , please try again")
            return redirect('home')
    return HttpResponse("404 - not Found")

def handlelogout(request):
        logout(request)
        messages.success(request,"Successfully Logged Out") 
        return redirect("home")






  
   
  
