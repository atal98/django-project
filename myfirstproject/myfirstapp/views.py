from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
# Create your views here.
def error_404_view(request,exception):
    return render(request,'404.html')
    
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name ,
        "age" : age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request, 'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = "Hello world"
    greeting = "Hey how are you ?"

    fruits = ["apple", "mango", "banana"]

    num1, num2 = 3, 5
    ans = num1 > num2 
    print(ans)
    mydictionary = {
        "var" : var, 
        "msg" : greeting ,
        "myfruits" : fruits ,
        "ans" : ans,
        "num1" : num1,
        "num2": num2
    }
    return render (request,'third.html', context = mydictionary)


def myimagepage(request):
    return render(request, 'image.html')

def myimagepage2(request):
    return render(request, 'image2.html')

def myimagepage3(request):
    return render(request, 'image3.html')

def myimagepage4(request):
    return render(request, 'image4.html')

def myimagepage5(request,imagename):
    myimagename =  str(imagename);
    myimagename =  myimagename.lower();
    print(myimagename)
    if myimagename == "tiger":
        var = True
    elif myimagename == "bird":
        var = False
    
    mydictionary = {
        "var": var
    }
    return render(request, 'image5.html', context= mydictionary)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mydictionary= {
        "var1 ": request.POST['mytext'],
        "var2": request.POST['mytextarea'],
        "method" : request.method

    }
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']

            mydictionary = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)
            import re
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)
            
            if errorflag != True:
                mydictionary["success"] = True
                mydictionary["successmsg"] = "Form Submitted"

            mydictionary["error"] = errorflag
            mydictionary["errors"] = Errors
            
            return render(request, 'myform2.html', context=mydictionary)
            

            
        
                
    elif request.method == "GET":
        form = FeedbackForm()
        mydictionary = {
            "form" : form
        }
        return render(request, 'myform2.html', context=mydictionary)
            
        
   







