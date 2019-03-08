from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'cwApp/index.html')
def p2(request):
    return render(request,'cwApp/page2.html')
def p3(request):
    return render(request,'cwApp/page3.html')
