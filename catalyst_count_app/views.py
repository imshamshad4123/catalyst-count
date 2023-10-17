from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import MyModel
# from .serializers import MyModelSerializer

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import csv
from . models import Company

# @api_view(['GET'])
# def mymodel_list(request):
#     queryset = MyModel.objects.all()
#     serializer = MyModelSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def mymodel_create(request):
#     serializer = MyModelSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @login_required(login_url='login_user')
def base(request):
    return render(request,"base.html")

# def login_user(request):
#     if request.method=="POST":
#         name=request.POST["username"]
#         # email=request.POST["email"]
#         password=request.POST["password"]

#         user=User.objects.get(username=name)

#         # user=authenticate(request,name,password)

#         print("===user===",user)
#         if user:
#             login(request,user)
#             print("==login",user)
#             return redirect('base')

#         else:
#         #     # user = User.objects.create_user(name, email, password)
#             return redirect('login_user')
#         # login(request,user)
#     print("====test====")
#     return render(request,"login.html")

def login_user(request):
    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"]

        # Use authenticate() to check if the provided credentials are valid
        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')  # Add a success message
            return redirect('base')  # Redirect to the desired URL after successful login
        else:
            messages.error(request, 'Invalid username or password.')  # Add an error message
            return redirect('login_user')  # Redirect back to the login page

    return render(request, "login.html")


def upload_data(request):
    if request.method == 'POST' and request.FILES['filedata']:
        csv_file = request.FILES['filedata']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            Company.objects.create(
                name=row['name'],
                domain=row['domain'],
                year_founded=row['year founded'],
                industry=row['industry'],
                size_range=row['size range'],
                locality=row['locality'],
                country=row['country'],
                linkedin_url=row['linkedin url'],
                current_employee_estimate=row['current employee estimate'],
                total_employee_estimate=row['total employee estimate']
            )
            print("===uploading===")
        return HttpResponse("uploaded successfully")
    return render (request,"upload_data.html")

def query_builder(request):
    return render(request,"query_builder.html")
    

def users(request):
    return render(request,"users.html")

def add_user(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]

        check_email = User.objects.filter(email=email)
        if check_email.exists():
            messages.warning(request, "Email already exist!")
            return HttpResponse("email already exist")

        else:
            user = User.objects.create_user(name, email, password)
    return render(request,"add_user.html")


def upload(request):
    
        # return render(request, 'success.html')
    return HttpResponse("uploaded")