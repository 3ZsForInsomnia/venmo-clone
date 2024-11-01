from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(max_length=100, index=True)
    password: str = Field(max_length=100)


class Account(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    balance: int = Field(default=0)
    user_id: int = Field(default=None, foreign_key="user.id")
    is_primary: bool = Field(default=False)


class Transaction(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    sender: int = Field(default=None, foreign_key="user.id")
    receiver: int = Field(default=None, foreign_key="user.id")
    created_by: int = Field(default=None, foreign_key="user.id")
    amount: int
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    approved_on: datetime = Field(default=None, nullable=True)
    approved: bool = Field(default=False)
