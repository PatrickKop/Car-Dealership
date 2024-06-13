from django.shortcuts import render, HttpResponse

# All below is added
def home(request):
    return render(request, "firstpage.html")

def second(request):
    return render(request, "secondpage.html")
    
