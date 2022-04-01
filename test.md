1- folder project
2- py -m venv env
3- env\Scripts\activate
4- pip install django
5- django-admin startproject Prj .
6- py manage.py startapp app
7- py manage.py migrate
8- py manage.py createsuperuser
9- app in installed in settings
10- templates , static
11- [ views , template , model ]
12- model >> Vacation
13- vacation [ employee , start_at , end_at ]
14 - views home
def home (request) :
    1- request.method=="POST":
        try : 
            1- save vacation 
            2- render html with pram (sas)

        except: 
            1- render html with pram (err)


    2- request.method!="POST":
        1- render html 


15- template 
    1- if sas >>> message succses
    2- if err >>> message error
    3- form method =="POST"


16- urls 
    path("",home,name="home")


17- authentication

    1- pip install all-auth
    2- instaled apps 
    3- authntication
    4- context_procces
    5- account template folder 
    6- urls path("account/",include("all-auth.urls"))

18- django-crispy-forms
    pip install 
    installed apps 
    package ="bootstrap4"
    load html




19- CustomUser
    class CustomUser(AbstractUser):
          mobile_number=IntegarField()



20- Signup Original >>> ["username","email","pasword","confirm_password"]   (V,T,U,M) (Signup,signup.html,accounts/signup/,User)
    Signup Fake     >>> ["username","email","password","mobile_number"]     (V,T,U,M) (Signup,signup.html,accounts/signup/,CustomUser)


21- (Fake) Signup Form
    class RegisterForm(ModelForm):
        class Meta:
            model=CustomUser
            fields=["username","email","password","mobile_number"]


22- (Fake) Signup Views


def Signup(request):
    if request.method=="POST":  
        form=RegisterForm(request.POST)     >>> {username:alsldaskldlas,email:aksjdnakjsdasd,password:asdasdas,mob:asdasdasdad}
        form.is_valid():
            new_user=CustomUser.objects.create_user(
                username=request.POST.get("username") 
            )
            new_user.save()
            return redirect (home)


23- (fake) Signup.html
    <form method="POST">
        {{form|crispy}}
    </form>

24- logout
    <form method="post" action="{% url 'account_logout' %}">
            {% csrf_token %}
            {% if redirect_field_value %}
            <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}"/>
            {% endif %}
            <button class="btn btn-danger w-100" type="submit">{% trans 'Sign Out' %}</button>
   </form>


