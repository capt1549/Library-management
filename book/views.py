# Create your views here.

from django.shortcuts import render
from django.shortcuts import render,redirect
from book.models import Books,RegisterAdmin, RegisterUser
from django.contrib import messages
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import BooksSerializer

class BookList(APIView):

    def get(self,request):
        book1=Books.objects.all()
        serializer=BooksSerializer(book1, many= True)
        return Response(serializer.data)

    def post(self,request):
        pass


def INDEX(request):
    emp=Books.objects.all()
    context={
        'emp':emp
    }
    return render(request,"admin.html",context)

def Add(request):
    if request.method=="POST":
        Book=request.POST.get('book')
        Author=request.POST.get('author')
        About=request.POST.get('about')
        Status=request.POST.get('status')
        Price=request.POST.get('price')
        Rating=request.POST.get('rating')
        View=request.POST.get('view')

        emp=Books.objects.create(
            book=Book,
            author=Author,
            about=About,
            status=Status,
            price=Price,
            rating=Rating,
            view=View
        )
        emp.save()
        context={
        'emp':emp
    }
        return redirect("home")
    return render(request,'admin.html',context)




def Edit(request):
    emp=Books.objects.all()

    context={
        'emp':emp
    }
    return redirect(request,'admin.html',context)


def Update(request,id):
    if request.method=="POST":
        book=request.POST.get('book')
        author=request.POST.get('author')
        about=request.POST.get('about')
        status=request.POST.get('status')
        price=request.POST.get('price')
        rating=request.POST.get('rating')
        view=request.POST.get('view')

        emp=Books(
            id=id,
            book=book,
            author=author,
            about=about,
            status=status,
            price=price,
            rating=rating,
            view=view,
        )
        emp.save()
        return redirect("home")
    return redirect(request,'admin.html')


def Delete(request,id):
    emp=Books.objects.filter(id=id)
    emp.delete()

    context={
        'emp':emp
    }
    return redirect('home')

#**************************Admin authentication****************************
def signupadmin(request):

    if request.method=="POST":
        Username=request.POST['username']
        Fname=request.POST['fname']
        Lname=request.POST['lname']
        Email=request.POST['email']
        Pass1=request.POST['pass1']
        Pass2=request.POST['pass2']
        Gender=request.POST['gender']

        if RegisterAdmin.objects.filter(username=Username):
            messages.error(request,"Username already exist! Please try another.")
            return redirect('signupuser')

        if RegisterAdmin.objects.filter(email=Email):
            messages.error(request,"Email already registered! Please try another.")
            return redirect('signupuser')

        if len(Username)>20:
            messages.error(request,"Username should not be greater than 20 characters.")
            return redirect('signupuser')

        if Pass1 != Pass2:
            messages.error(request,"Password didn't matched. ")
            return redirect('signupuser')

        user= RegisterAdmin.objects.create(
            username=Username,
            fname=Fname,
            lname=Lname,
            email=Email,
            pass1=Pass1,
            pass2=Pass2,
            gender=Gender,
        )
        user.save()
        return redirect('admin_login')
    else:
        return render(request,'adminsignup.html')


def loginadmin(request):
    try:
        if request.method=="POST":

            Username= request.POST['username']
            Pass1=request.POST['pass1']

            user=RegisterAdmin.objects.get(username=Username,pass1=Pass1)
            if Username:
                if user.pass1==Pass1:
                    return redirect('home')
                else:
                    messages.error(request,"Incorrect Password")
                    return redirect('signin')
            else:
                    messages.error(request,"Incorrect Username")
                    return redirect('signin')
    except:
            messages.error(request,"Bad credentials")
            return redirect('signin')

#****************************************User authentication******************************
def signupuser(request):
    
    if request.method=="POST":
        Username=request.POST['username']
        Fname=request.POST['fname']
        Lname=request.POST['lname']
        Email=request.POST['email']
        Pass1=request.POST['pass1']
        Pass2=request.POST['pass2']
        Gender=request.POST['gender']

        if RegisterUser.objects.filter(username=Username):
            messages.error(request,"Username already exist! Please try another.")
            return redirect('signupuser')

        if RegisterUser.objects.filter(email=Email):
            messages.error(request,"Email already registered! Please try another.")
            return redirect('signupuser')

        if len(Username)>20:
            messages.error(request,"Username should not be greater than 20 characters.")
            return redirect('signupuser')
        

        if Pass1 != Pass2:
            messages.error(request,"Password didn't matched. ")
            return redirect('signupuser')

        user= RegisterUser.objects.create(
            username=Username,
            fname=Fname,
            lname=Lname,
            email=Email,
            pass1=Pass1,
            pass2=Pass2,
            gender=Gender,
        )
        user.save()
        return redirect('signin')
    else:
        return render(request,'usersignup.html')

def loginuser(request):
    try:
        if request.method=="POST":
            Username= request.POST['username']
            Pass1=request.POST['pass1']

            user=RegisterUser.objects.get(username=Username,pass1=Pass1)
            if Username:
                if user.pass1==Pass1:
                    return redirect('user')
                else:
                    messages.error(request,"Incorrect Password")
                    return redirect('signin')
            else:
                    messages.error(request,"Incorrect Username")
                    return redirect('signin')
    except:
            messages.error(request,"Bad credentials")
            return redirect('signin')
# *********************************************************************************************************************

def signin(request):
    return render(request,"userlogin.html")

def signup(request):
    return render(request,'usersignup.html')
    
def signout(request):
    return render(request,"userlogin.html")

def signoutadmin(request):
    return render(request,"adminlogin.html")

def user(request):
    emp=Books.objects.all()
    context={
        'emp':emp
    }
    return render(request,"user.html",context)

def admin_login(request):
    return render(request,"adminlogin.html")

def admin_signup(request):
    return render(request,"adminsignup.html")
