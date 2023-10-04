from django.shortcuts import render
from dapp.models import Entries

# Create your views here.


def index(request):
    
    if request.method=='POST':
        wd = request.POST['word']
        data = Entries.objects.filter(word=wd).values

        context = {'data':data}

    
    return render(request,'index.html',context)