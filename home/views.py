from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q



# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST.get('dept', None)
        role = request.POST.get('role', None)
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'home.html')
    else:
        return HttpResponse('An Exception Occurred')

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept= int(request.POST['dept'])
        role = int(request.POST['role'])

        dept1 = get_object_or_404(Department, id=dept)
        role1 = get_object_or_404(Role, id=role)
        print(dept1 , role1)

        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,  dept=dept1,role=role1, hire_date = datetime.now())
        new_emp.save()
        message = 1
        con = {'c' : message}
        return render(request, 'add_emp.html' ,con )
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    
   

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    
    return render(request , 'all_emp.html' , context)

def remove_emp(request , emp_sno=0 ):
    if emp_sno:
        emp_to_removed = Employee.objects.get(sno=emp_sno)
        emp_to_removed.delete()
        message = 1
        con = {'c' : message}
        return render(request , 'remove_emp.html', con)
      
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    
    return render(request, 'remove_emp.html',context)

