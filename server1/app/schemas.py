from pydantic import BaseModel, Field


class EmployeeBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    age: int
    position: str = Field(max_length=250)
    remote: bool


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
