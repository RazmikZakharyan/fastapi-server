from sqlalchemy.orm import Session

from . import models, schemas


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()


def get_employees_by_name(db: Session, first_name: str):
    return db.query(models.Employee).filter(
        models.Employee.first_name == first_name
    ).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_user = models.Employee(**employee.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
