from django.shortcuts import render

# Create your views here.
def index(request): #sends user to page 1
    return render(request,'cwApp/index.html')
def p2(request): #sends user to page 2
    return render(request,'cwApp/page2.html')
def p3(request):#sends user to page 3
    return render(request,'cwApp/page3.html')
