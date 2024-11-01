from pydantic import BaseModel


class AccountBase(BaseModel):
    balance: int
    is_primary: bool
    name: str


class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str
    starting_balance: int
    first_account_name: str


class UserLoginPost(BaseModel):
    username: str
    password: str


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserLoginResponse(BaseModel):
    user: User
    accounts: list[Account] = []


class TransactionPost(BaseModel):
    amount: int
    created_by: int
    # Transactions between a user's own accounts are instantly approved
    between_user_accounts: bool


class TransactionBase(BaseModel):
    amount: int
    sender: int
    receiver: int
    created_by: int
    created_on: str
    approved: bool
    approved_on: str


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True


# List of transactions for a user
# Includes transactions between a user's own accounts, and transactions to other users
class TransactionHistory(Transaction):
    transactions: list[Transaction] = []
