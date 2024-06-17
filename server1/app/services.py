from typing import List, Optional
from sqlmodel import Session
from .models import EmployeeBase, Employee
from .db import engine, create_db_and_tables
from fastapi import HTTPException


class EmployeeService:
    def __init__(self):
        create_db_and_tables()

    def create_employee(self, employee_data: EmployeeBase) -> Employee:
        new_Employee = Employee(**employee_data.dict())
        with Session(engine) as session:
            session.add(new_Employee)
            session.commit()
            session.refresh(new_Employee)
        return new_Employee

    def get_all_employees(self) -> List[Employee]:
        with Session(engine) as session:
            return session.query(Employee).all()

    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        with Session(engine) as session:
            employee = session.get(Employee, employee_id)
            if not employee:
                raise HTTPException(status_code=404, detail="Employee not found")
            return employee

    def get_employees(self, **kwargs) -> List[Employee]:
        with Session(engine) as session:
            data = {key: value for key, value in kwargs.items() if value}
            employees = session.query(Employee).filter_by(**data).all()
            if not employees:
                raise HTTPException(status_code=404, detail="Employee not found")
            return employees

    def delete_employee(self, employee_id: int) -> bool:
        with Session(engine) as session:
            employee = session.get(Employee, employee_id)
            if employee:
                session.delete(employee)
                session.commit()
                return True
        return False
