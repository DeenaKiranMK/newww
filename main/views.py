from django.shortcuts import render, redirect ,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    employee=Employee.objects.all()
    return render(request,'emp_list.html',{'employee':employee})

def add_employee(request):
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmployeeForm()

    return render(request,'add_emp.html',{'form':form})

def delete_emp(request,pk):
    employee=get_object_or_error_404(Employee,pk=pk)
    if request.method =='POSt':
        employee.delete()
        return redirect('emp_list')
    return render(request,'delete_emp.html',{'employee':employee})