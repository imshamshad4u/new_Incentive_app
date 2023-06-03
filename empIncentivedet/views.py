# from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
import re
import json
import requests
from .models import employee
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
# from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from .serializers import employeeSerializer
# Create your views here.


class employeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

# @csrf_exempt
# def home(request):

#     test = employee.objects.all()

#     if request.method == 'POST':
#         empname = request.POST['empname']
#         empemail = request.POST['empemail']

#         empdept = request.POST['empdepartment']
#         desc = request.POST['empdesc']

#         empfile = request.FILES.get('fileupload')

#         email = employee.objects.filter(EmpEmail=empemail)

#         if email.exists():
#             messages.warning(request, "Email already exist!",
#                              extra_tags="alert-warning")
#             return redirect('/')

#         newemp = employee(EmpName=empname, EmpEmail=empemail,
#                           EmpDepartment=empdept, EmpDescription=desc, EmpFile=empfile)
#         newemp.save()

#     context = {
#         "test": test,

#     }

#     return render(request, "main.html", context)


# def getdetails(request):
#     # response = request.get('').json()
#     # response = employee.objects.values_list("id", "EmpName")
#     # response=employee.objects.filter('EmpEmail'=)
#     # response = employee.objects.get(id=id)
#     # context = {'response': response}
#     # print(response)
#     return render(request, 'incentiveform.html')

# # @csrf_exempt


# def register(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')

#         email = request.POST.get('useremail')
#         password = request.POST.get('password')

#         email = employee.objects.filter(EmpEmail=email)
#         if email.exists():
#             messages.warning(request, "Email already exist!",
#                              extra_tags="alert-warning")
#             return redirect('/')

#             # user = User.objects.create_user(
#             #     EmpName=name,
#             #     EmpEmail=email,
#             #     EmpPass=password
#             # )

#             # user.set_password(password)
#             # user.save()
#             newemp = employee(EmpName=empname, EmpPass=password)
#             newemp.save()

#         messages.success(
#             request, "Account Created Successfully.", extra_tags="alert-success")

#         return redirect('login')
#     return render(request, 'register.html')


# def login(request):
#     if request.method == 'POST':
#         useremail = request.POST.get('email')
#         password = request.POST.get('password')
#         useremail = employee.objects.filter(EmpEmail=useremail)
#         if useremail.exists():

#             return redirect('/home')
#         else:
#             return redirect('/login')
#     return render(request, 'login.html')
# # class employeeViewSet(viewsets.ModelViewSet):
# #     queryset = employee.objects.all()
# #     serializer_class = employeeSerializer
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         useremail = request.POST['useremail']
#         userpassword = request.POST['password']
#         user = User.objects.create_user(
#             'username', 'useremail', 'userpassword')
#         user.save()
#         messages.success(request, 'Account is created successfully')
#         return redirect('/login')
#     return render(request, 'register.html')

# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         useremail=request.POST['useremail']

########new#######
# Create your views here.

def user_type(request):
    return render(request, 'user_type.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['useremail']
        password = request.POST['password']
    # user=request.User.get
        check_email = User.objects.filter(email=email)
        if check_email.exists():
            messages.warning(request, "Email already exist!")
            return redirect('register')

        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(
                request, "Your account has been created successfully!")
            return redirect('loginuser')
    return render(request, 'register.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        # useremail = request.POST['email']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "requirement not satisfied")
            return redirect('loginuser')

    return render(request, 'login.html')

# def home(request):
#     return render(request,'home.html')


def main(request):
    # context = {
    #     "path": 'getdetails'
    # }
    # return render(request, 'main.html', context)
    return render(request, 'main.html')


@login_required(login_url='loginuser')
def logoutuser(request):
    logout(request)
    return redirect('loginuser')


def getdetails(request, id=None):

    if request.method == 'POST':
        empname = request.POST['empname']

        empemail = request.POST['empemail']

        empdept = request.POST['empdepartment']
        desc = request.POST['empdesc']

        empfile = request.FILES.get('fileupload')
        admin_email = User.objects.filter(email=empemail)
        email = employee.objects.filter(EmpEmail=empemail)
        if admin_email.exists():
            return render(request, 'home.html')
        else:
            if email.exists():
                messages.warning(request, "Email already exist!",
                                 extra_tags="alert-warning")
                return redirect('loginuser')
            else:
                newemp = employee(EmpName=empname, EmpEmail=empemail,
                                  EmpDepartment=empdept, EmpDescription=desc, EmpFile=empfile)
                newemp.save()
                messages.success(request, "form submitted successfully!!!",
                                 extra_tags="alert-success")
        return redirect('main')
    return render(request, 'home.html')


def index(request, id=None):

    response = employeeViewSet()
    answer = response.queryset.values()
    cur_department = ''
    if request.method == "POST":
        cur_department = request.POST['empdepartment']
    if cur_department == "all":
        answer = response.queryset.values()
        # answer=employee.objects.all()
    elif cur_department == 'IT':
        answer = employee.objects.filter(EmpDepartment=cur_department)
    elif cur_department == 'HR':
        answer = employee.objects.filter(EmpDepartment=cur_department)
    elif cur_department == 'Accounts':
        answer = employee.objects.filter(EmpDepartment=cur_department)
    elif cur_department == 'Finance':
        answer = employee.objects.filter(EmpDepartment=cur_department)

    # request module logic

    # print('answerrrrrrr', answer)
    # print(answer)
    # URL = 'http://127.0.0.1:8000/employee/'
    # data = {}
    # if id is not None:
    #     data = {'id': id}
    # json_data = json.dumps(data)
    # r = requests.get(url=URL, data=json_data)
    # r = requests.get(URL)
    # print('rrrrrrrrrrrrrrrrrrrrr', r)
    # data = r.json()
    # print("jjjjjjssoonnnnnn", data)

    # print(data)
    # query=employee.objects.filter(data[0]['EmpDepartment'])

    # result=list(query.values())

    # print("myqrrrrryyyyyyyyyyy",result)
    # for i in data[0].items():
    #     print(i.empname)
    #     break
    # data = dict(data)
    # print(data[0]['EmpName'])

    # context = {
    #     'answer': answer
    # }
    context = {
        'answer': answer
    }

    return render(request, 'index.html', context)


def deleteuser(request, id):
    user = employee.objects.get(id=id)
    print('userrrrrrrrrrrrr is:', user)
    user.delete()
    # URL = 'http://127.0.0.1:8000/employee/{id}/'

    # r = requests.get(URL)
    # print('rrrrrrrrrrrrrrrrrrrrr', r)
    # data = r.json()
    # print("jjjjjjssoonnnnnn", data)
    return render(request, 'home.html')


def updateuser(request, id):
    # getdetails(request, id)
    queryset = employee.objects.get(id=id)
    print('querrryyyyy', queryset)

    if request.method == "POST":
        data = request.POST
        name = data.get('empname')
        email = data.get('empemail')
        department = data.get('empdepartment')
        empfile = request.FILES.get('fileupload')

        queryset.EmpName = name
        queryset.EmpEmail = email

        if empfile:
            queryset.EmpFile = empfile

        queryset.save()
        return render(request, 'home.html')

    # ... and other fields you need
    # print('contextttttttttttt: ', context)
    # print('userrrrrrrrrrrrr is:', user)
    # user.delete()
    # URL = 'http://127.0.0.1:8000/employee/{id}/'

    # r = requests.get(URL)
    # print('rrrrrrrrrrrrrrrrrrrrr', r)
    # data = r.json()
    # print("jjjjjjssoonnnnnn", data)
    return render(request, 'update.html')
