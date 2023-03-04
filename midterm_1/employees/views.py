# Create your views here.
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from employees.models import Employees
from employees.serializers import EmployeesSerializer


@csrf_exempt
def employees_handler(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = EmployeesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_employee(pk):
    try:
        employee = Employees.objects.get(id=pk)
        return {
            'status': 200,
            'employee': employee
        }
    except Employees.DoesNotExist as e:
        return {
            'status': 404,
            'employee': None
        }


@csrf_exempt
def employee_handler(request, pk):
    result = get_employee(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Employee not found'}, status=404)

    employee = result['employee']

    if request.method == 'GET':
        serializer = EmployeesSerializer(employee)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = EmployeesSerializer(data=data, instance=employee)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        employee.delete()
        return JsonResponse({'message': 'Employee deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)
