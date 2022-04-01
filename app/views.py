from django.shortcuts import redirect, render
from app.models import CustomUser, Vacation

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User

from .forms import RegisterForm


def Signup(request):
    register_form = RegisterForm()
    err=""
    if request.method=='POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"],mobile_number=request.POST["mobile_number"])
            new_user.save()  
            err=None
            return redirect(Home)
        else:
            err="err"
            
        
    return render (request,'account/signup.html',{'form':register_form,"err":err})
    



# def Login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#         else:
#             print("sucsses")
#     print("not post")        
#     return render(request,'index.html')





@login_required
def Home(request):
    
    if request.method=="POST":
        reason=request.POST.get("reason")
        start_at=request.POST.get("from")
        end_at=request.POST.get("to")
        user=request.user
    
        try:
            
            vac=Vacation.objects.create(
                employee=user,
                start_at=start_at,
                end_at=end_at,
                reason=reason
            )
    
            vac.save()
            print("succc")
            return render(request,"index.html",{"sas":"submited"})

            
        except Exception as e:
            return render(request,"index.html",{"err":e})

    
    return render(request,"index.html")

