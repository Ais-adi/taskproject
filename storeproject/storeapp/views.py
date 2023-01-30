from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils.safestring import mark_safe

from storeapp.forms import PersonCreationForm
from storeapp.models import Courses, Person


def home(request):
    return render(request,"home.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # cpassword = request.POST['cpassword']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,"newpage.html")
        else:
            messages.info(request,"Invalid Credentials")
        return redirect('login')
    return render(request,"login.html")

def register(request):
     if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
          if User.objects.filter(username=username).exists():
               messages.info(request,"USERNAME ALREADY EXISTS")
               return redirect('register')

          else:
              user=User.objects.create_user(username=username, password=password)
              user.save();
              return redirect ('/login')
              print("user created")
        else:
            messages.info(request,"password not matching")
        return redirect('/register')
     return render(request, 'register.html')

# def person_create_view(request):
#         # user1 = request.POST.get or None
#
#         # Get user member profile instance
#         instance = get_object_or_404(Person)
#
#         form = PersonCreationForm(request.POST or None, instance=instance)
#
#         context = {
#             "form": form,
#             "instance": instance
#         }
#
#         if form.is_valid():
#             # ...
#             return redirect('/add')
#         else:
#             # Initial form display, and redisplay of invalid form
#             return render(request, 'form.html',context )




def person_create_view(request):
    # ins =Materials_provide.objects.get(pk=pk)

    form = PersonCreationForm()
    # form1=ClassNameForm(instance=ins)

    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        # form1=form1(request.POST,instance=ins)
        # materials_provide = request.POST.get('materials')
        # Person.objects.create(materials_provide=materials_provide)
        languages = request.POST.getlist('languages')
        if form.is_valid():
          # if form1.is_valid():
            form.save()
            # form1.save()
            messages.info(request,mark_safe( "<center><b>Recorded Successfully <br><a href='/home'>GO TO Home</a><b></center"))

            return redirect('/add')
    return render(request, 'form.html', {'form': form})
def load_courses(request):
    department_id = request.GET.get('department_id')
    course = Courses.objects.filter(department_id=department_id).all()
    return render(request, 'courses.html', {'course': course})
def logout(request):
    auth.logout(request)
    return redirect('/login')