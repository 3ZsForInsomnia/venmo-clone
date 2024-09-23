from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    balance: int
    starting_balance: int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    note: str
    amount: int
    sender: int
    receiver: int


class Transaction(TransactionBase):
    id: int
    created_by: int
    created_at: str
    completed_at: str
    updated_at: str

    class Config:
        orm_mode = True
