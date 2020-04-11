from django.shortcuts import HttpResponse

def homePageView(request):
    return HttpResponse('Hello')
def index(request):
    return render(request, 'main/index.html')
def info(request):
    return render(request, 'main/other.html')
def login(request):
    return render(request, 'main/login.html')

# Create your views here.
