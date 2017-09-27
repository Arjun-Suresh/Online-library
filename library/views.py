import pymysql
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from .models import Users
from django.conf import settings
from django.http import HttpResponseForbidden

connection = pymysql.connect(host=settings.DATABASES['default']['HOST'],
                             user=settings.DATABASES['default']['USER'],
                             password=settings.DATABASES['default']['PASSWORD'],
                             db=settings.DATABASES['default']['NAME'])




def redirectToPage(request,message,url):
    messages.add_message(request, messages.INFO, message)
    return redirect(url)

    
def index(request,arg='',context={}):
    request.session['userEmail']='#'
    request.session['Password']='#'
    request.session['userType']='#'
    return render(request, 'library/index.html', context)


def checksignup(request,arg=''):
    userEmail=request.POST.get("User_email")
    userName=request.POST.get("User_name")
    Password=request.POST.get("password")
    if userEmail == None or Password == None or userName == None:
        raise Http404
    sql="SELECT * from users where email='"+userEmail+"'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        returnedVal = cursor.fetchone()
    if returnedVal == None:
        sql="INSERT into users values('"+userEmail+"','"+userName+"','"+Password+"','normal')"
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql)
            except:
                return redirectToUserLoginPage(request, "Please fill the details again", '/library/user/signup')
        connection.commit()
        request.session['userEmail']=userEmail
        request.session['Password']=Password
        request.session['userType']='normal'
        return redirect("/library/user/home")
    else:
        return redirectToPage(request, "Email already present. Try with a different one.", '/library/user/signup')

    
def userloginoption(request,arg='',context={}):
    return render(request, 'library/user/loginoption.html', context)


def userlogin(request,arg='',context={}):
    return render(request, 'library/user/login.html', context)

def signup(request,arg='',context={}):
    return render(request, 'library/user/signup.html', context)

def adminlogin(request,arg='',context={}):
    return render(request, 'library/admin/login.html', context)

def userhome(request,arg='', context={}):
    if 'userEmail' in request.session and 'Password' in request.session:
        if request.session['userEmail'] == '#' or request.session['Password'] == '#':
            return redirectToPage(request,"Please Login to proceed", '/library/user/loginoption')
        else:
            return render(request, 'library/user/home.html', context)
    else:
        return redirectToPage(request,"Please Login to proceed", '/library/user/loginoption')
    

def userauthenticate(request,arg=''):
    userEmail=request.POST.get("User_Email")
    Password=request.POST.get("User_Password")
    if userEmail == None or Password == None:
        raise Http404
    sql="SELECT userpassword from users where email='"+userEmail+"'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        returnedPassword = cursor.fetchone()
    if returnedPassword != None and returnedPassword[0] == Password:
        request.session['userEmail']=userEmail
        request.session['Password']=Password
        request.session['userType']='normal'
        return redirect("/library/user/home")
    else:
        return redirectToPage(request, "Login failure. Please try again", '/library/user/login')

def userbooksearch(request,arg='',context={}):
    if 'userEmail' in request.session and 'Password' in request.session:
        if request.session['userEmail'] == '#' or request.session['Password'] == '#':
            return redirectToPage(request,"Please Login to proceed", '/library/user/loginoption')
        else:
            return render(request, 'library/user/booksearch.html', context)


def adminauthenticate(request,arg=''):
    userEmail=request.POST.get("User_Email")
    Password=request.POST.get("User_Password")
    if userEmail == None or Password == None:
        raise Http404
    sql="SELECT userpassword,usertype from users where email='"+userEmail+"'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        returnedList = cursor.fetchone()
    if returnedList != None and returnedList[0] == Password and returnedList[1]=='admin':
        request.session['userEmail']=userEmail
        request.session['Password']=Password
        request.session['userType']='admin'
        return redirect("/library/admin/home")
    else:
        return redirectToPage(request,"Login failure. Please try again", '/library/admin/login')


def adminhome(request,arg='', context={}):
    if 'userEmail' in request.session and 'Password' in request.session and 'userType' in request.session:
        if request.session['userEmail'] == '#' or request.session['Password'] == '#' or request.session['userType'] == '#':
            return redirectToAdminLoginpage(request,"Please Login to proceed")
        if request.session['userType'] != 'admin':
            return HttpResponseForbidden()
        else:
            return render(request, 'library/admin/home.html', context)
    else:
        return redirectToPage(request,"Please Login to proceed", '/library/admin/login')


def logout(request,arg='',context={}):
    return redirect('/library/')
    
