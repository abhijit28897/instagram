from django.shortcuts import render,get_object_or_404
from .models import Picture
from django.core.paginator import Paginator   #paginator
# Create your views here.
def index(request):
    return render (request,'index.html')

def home(request):
    pics= Picture.objects.all()   #get all objects
    paginator = Paginator(pics, 3) #obj of paging

    page = request.GET.get('page') #page number
    pictures =paginator.get_page(page) # get next set of img

    return render(request,'home.html',{'pictures':pictures})

def detail(request,id):
    pic= get_object_or_404(Picture,pk=id)
    return render(request,'upload.html',{'pic':pic})
