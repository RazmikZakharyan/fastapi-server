from sqlmodel import SQLModel, Field
from typing import Optional


class EmployeeBase(SQLModel):
    first_name: str
    last_name: str
    age: int
    position: str
    remote: bool
    photo: str


class Employee(EmployeeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
