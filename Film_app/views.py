from django.shortcuts import render,get_object_or_404,redirect
from .models import Dawrat,PostMainHome ,Offre ,Comments ,Command
from .urls import *
from django.core.paginator import Paginator

# Create your views here.





def home(request):


    dawrat = Dawrat.objects.all()


    paginator = Paginator(dawrat,6)

    page_nember = request.GET.get('page')
    
    page_obj = paginator.get_page(page_nember)
    
    item_name = request.GET.get('bbw')

    if item_name != '' and item_name is not None:

        page_obj = Dawrat.objects.filter(title__icontains = item_name)

    return render(request,'home.html',{'dawrat':page_obj})



def homme(request):

    postMainHome = PostMainHome.objects.all()

    return render(request,'homme.html',{'PostMainHome':postMainHome})



def detail(request,myid):


    dawrat_detail = get_object_or_404(Dawrat,id=myid)

    com = Comments.objects.all()

    if request.method == 'POST':

        email = request.POST['email']
        name = request.POST['name']
        comment = request.POST['comment']
        
        comments = Comments.objects.create(
            email =email,
            text_comment = comment,
            name = name,
        )

        return redirect('course')

    return render(request,'detail.html',{'dawrat_detail':dawrat_detail, 'com':com})





def apell_nous(request,):


    return render(request,'apell_nous.html',)







def plus_info(request,):


    return render(request,'plus_info.html',)







def ofre(request,):

    ofre = Offre.objects.all()

    return render(request,'ofre.html',{'ofre':ofre})








def command(request):

    if request.method == 'POST':

        
        name = request.POST['name']
        prenom = request.POST['prenom']
        email = request.POST['email']
        num = request.POST['num']


        comments = Command.objects.create(

            
            name = name,
            prenom =prenom,
            email =email,
            num = num,

        )
        return redirect('confarmation')
        

    return render(request,'command.html')





def confarmation(request):


    return render(request,'confirm_comond.html')