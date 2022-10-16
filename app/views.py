from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import UserAccount ,Post
from django.contrib import messages
from django.shortcuts import redirect, render


# Create your views here.

def userLogin(request):
    if request.method == 'POST':
        username    = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None :
            login(request,user)
            return redirect('userProfile')
        else:
            messages.error(request,'invalid credentials')
            return redirect("userProfile")

    return render(request,'signinuser.html')



def userProfile(request):
    
    user = UserAccount.objects.get(username = request.user)
    mypost = Post.objects.filter(user = user)

    context = {
        'user' : user,
        'mypost':mypost
    }
    return render(request,"userprofile.html",context)
        

def uploadPost(request):
    if request.method == "POST":

        imageupload =  request.FILES.get('img')
        if imageupload :

        # desc = request.POST['desc']
            this_user = UserAccount.objects.get(username = request.user)

            new_post = Post(image = imageupload ,user = this_user)
            new_post.save()

        else:
            messages.error(request, "NO FILE SUBMITTED", extra_tags='signupusername')
        

        return redirect("userProfile")


def userSignup(request):
    if request.method == "POST":
        username    = request.POST['username']
        email    = request.POST['email']
        location    = request.POST['location']
        state    = request.POST['state']
        gender    = request.POST['gender']
        password   = request.POST['password']
        if UserAccount.objects.filter(username = username).exists():
            print('GETTING INTO USERNAME')
            messages.error(request, "Username already taken", extra_tags='signupusername')
            return redirect(userSignup)

        UserAccount.objects.create_user(username= username,email =email ,location=location,state=state,gender=gender,password=password)

        return redirect("userLogin")

    return render (request,"usersignup.html")



def profileEdit(request,id):
    user= UserAccount.objects.get(id = id)
    if request.method == "POST":
        

        user.email = request.POST['email']
        user.location = request.POST['location']
        user.state = request.POST['state']
        user.gender = request.POST['gender']

        user.save()
        return redirect("userProfile")

    return render(request , "editprofile.html" ,{"user":user})

def shorts(request):
    post = Post.objects.all()
    return render(request, "shorts.html" ,{"post":post})

def userLogout(request):
    logout(request)
    return redirect("userLogin")

