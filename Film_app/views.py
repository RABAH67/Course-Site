from django.shortcuts import render,get_object_or_404,redirect
from .models import Dawrat,PostMainHome ,Offre ,Comments ,Command ,Profil
from .urls import *
from django.core.paginator import Paginator
from .forms import SingupForm ,UserForm,ProfileForm
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required

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







@login_required
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














def signup(request):
    if request.method=="POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('profile')
    else:
        form = SingupForm()
    return render(request,'singin.html',{'form':form})






def profile(request):
    
    profile= Profil.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profile':profile})



def profile_edit(request):
    
    profile= Profil.objects.get(user=request.user)
    
    if request.method=="POST":
        
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,instance=profile)
        
        if userform.is_valid() and profileform.is_valid():
            
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('profile')
        
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    
    return render(request,'profile/edit_profile.html',{'userform': userform  , 'profile':profileform})