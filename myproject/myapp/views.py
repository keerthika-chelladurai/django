from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def hello(request):
     return  HttpResponse("Hello, Welcome to my django app!")
 
def welcome(request):
     return  HttpResponse("my first django app!")
 
def display(request):
     return  HttpResponse("<h1>I Love Family</h1>")
 
def student(request,id):
    return HttpResponse(f"student ID is {id}")

def studentname(request, id, name):
    return HttpResponse(f"Student ID: {id}, Name: {name}")
       
  #template day -2   
    
def students(request):
    context = {
        "name":"Keerthika",
        "age":21
    }  
    return render(request,"student.html" ,context) 
    
    
    
 #day-2
def studentprofile(request):
    students = [
        {
            "name": "Ravi",
            "age": "22",
            "course": "Python Full Stack",
            "city": "Chennai"
        },
        {
          "name": "Priya",
          "age": "27",
          "course": "Java Full Stack",
          "city": "Coimbatore"  
        },
        {
            "name": "Keerthika",
            "age": "21",
            "course": "Python Full Stack",
            "city": "Tirupur"
        },
        {
            "name": "Revathi",
             "age": "45",
             "course": "Data Science",
            "city": "Madurai"
        },
        {
            "name": "Alagar",
            "age": "25",
            "course": "Python Full Stack",
             "city": "Trichy"
        }
    ]  
    context ={
        "students": students
    } 
    return render(request,"studentprofile.html",context)


# day 3 GET /POST METHOD
def studentform(request):
    
    if request.method == "POST":
        
         name = request.POST["name"]
         age = request.POST["age"]
         course = request.POST["course"]
         city = request.POST["city"]
        
         context = {
            "name": name,
            "age": age,
            "course": course,
            "city": city,
            "form_type":"post"
        }
         return render(request,"result.html",context)
    return  render(request, "studentform.html")

from django.shortcuts import render

def studentformget(request):
    if request.GET.get("name"):
         
         name = request.GET.get("name")
         age = request.GET.get("age")
         course = request.GET.get("course")
         city = request.GET.get("city")
         
         context ={
             "name":name,
             "age":age,
             "course":course,
             "city":city,
             "form_type":"get"
         }
         return render(request,"result.html",context)
    return  render(request,"studentformget.html")

# day 7 models


from django.shortcuts import render,redirect,get_object_or_404

from.models import student

from django.contrib import messages

# create your views here

#create

def create_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        course = request.POST["course"]
        
        student.objects.create(
            name=name,
            age=age,
            course=course
        )
        messages.success(request,"Student added successfully!")
        
        return redirect("students")
    return render(request,"student_form.html")


# READ

def student_list(request):
    students = student.objects.all()
    return render(
        request,
        "student_list.html",
        {"students":students}
    )
    

# UPDATE

def update_student(request, id):
    student_obj = get_object_or_404(student, id=id)

    if request.method == "POST":
        student_obj.name = request.POST["name"]
        student_obj.age = request.POST["age"]
        student_obj.course = request.POST["course"]

        student_obj.save()

        messages.success(
            request,
            "Student updated successfully!"
        )

        return redirect("students")

    return render(
        request,
        "student_form.html",
        {"student": student_obj}
    )


# DELETE

def delete_student(request, id):
    student_obj = get_object_or_404(student, id=id)

    student_obj.delete()

    messages.success(
        request,
        "Student deleted successfully!"
    )

    return redirect("students")




"""
Django Messages
     ⇩
messages.success()
messages.info()
messages.warning()
messages.error()
     ⇩
Template
     ⇩      
{% if messages %}
     ⇩
{% for message in messages %}    
     ⇩
{{ message }} 
     ⇩
Alert displayed             

"""
        
        