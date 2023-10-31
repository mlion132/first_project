from django.shortcuts import render
 
def first_page(request):
    return render(request,"core/first_page.html")
def second_page(request):
    return render(request,"core/second_page.html")
    
