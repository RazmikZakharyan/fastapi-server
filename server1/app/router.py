from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status, UploadFile
from .models import EmployeeBase, Employee
from .services import EmployeeService

import requests

router = APIRouter()


def get_Employee_service():
    return EmployeeService()


@router.post("/employee/new/", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeBase, employee_service: EmployeeService = Depends(get_Employee_service)):
    return employee_service.create_employee(employee)


@router.get("/employee/list/", response_model=List[Employee], status_code=status.HTTP_200_OK)
def filter_employee(
        first_name: str, position: str | None = None, remote: bool | None = None,
        employee_service: EmployeeService = Depends(get_Employee_service)
):
    employee = employee_service.get_employees(
        first_name=first_name, position=position, remote=remote
    )
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.get("/employees/", response_model=List[Employee], status_code=status.HTTP_200_OK)
def read_employees(employee_service: EmployeeService = Depends(get_Employee_service)):
    return employee_service.get_all_employees()


@router.get("/employees/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def read_employee(employee_id: int, employee_service: EmployeeService = Depends(get_Employee_service)):
    employee = employee_service.get_employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, employee_service: EmployeeService = Depends(get_Employee_service)):
    employee_service.delete_employee(employee_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/employees/image")
def employee_image(file: UploadFile):
    data = {'file': str(file.read())}
    r = requests.post('http://127.0.0.1:9002/employee_id', files=data)

    return r.json()
