from django.shortcuts import render

# Create your views here.
def rocky(request):
    d={'a':20,'b':30,'c':50}
    return render(request,'condtions.html',d)





def bhai(request):
    d={'name':'darling'}
    return render(request,'loop.html',d)