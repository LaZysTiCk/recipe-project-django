from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h1> Hello from DJANGO Server ... </h1>')


    return render(request,'home/index.html')

def contact(request):
    context = {'page': 'Contact Page'}
    return render(request,'home/contact.html',context)

def about(request):
    context = {'page' : 'About Page'}
    return render(request,'home/about.html',context)

def success_page(request):
    print("#" * 50)
    return HttpResponse("""<h1>Hi, This is a Success Page !!!!</h1>
                        <p> This is a paragraph </p>
                        <hr>
                        <h3 style="color:blue"> Hi this is an h3 tag inside view </h3>
                        """)