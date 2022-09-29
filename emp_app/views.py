from django.shortcuts import render, HttpResponse
from .models import Employee, Role ,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request, 'emp_app/index.html', context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=request.POST['role']
        phone=int(request.POST['phone'])
        location=request.POST['location']
        new_employee = Employee(first_name=first_name, last_name=last_name, dept_id = dept, salary=salary, bonus=bonus, role_id = role, phone=phone, location = location, hire_date = datetime.now())
        new_employee.save()
        return HttpResponse("<h3>Employee Added Successfully!</h3>")
    elif request.method == "GET":
        return render(request, 'emp_app/add_emp.html')
    else:
        return HttpResponse("Something Went Wrong!!!")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except:
            return HttpResponse("Please Enter a valid Employee ID")
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request, 'emp_app/remove_emp.html', context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context = {'emps':emps}
        return render(request, 'emp_app/index.html', context)
    elif request.method == "GET":
        return render(request, 'emp_app/filter_emp.html')
    else:
        return HttpResponse("Something Went Wrong!")
    return render(request, 'emp_app/filter_emp.html', context)
