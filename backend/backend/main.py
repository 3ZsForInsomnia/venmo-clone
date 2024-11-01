from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend import crud, db, schemas

origins = ["http://localhost:3000"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    db.create_db_and_tables()


@app.post("/login")
async def login(credentials: schemas.UserLoginRequest, session: db.SessionDep):
    user_found = crud.login(credentials.username, credentials.password, session)

    return user_found or {"message": "User not found"}


@app.post("/users")
async def create_user(user: schemas.UserCreate, session: db.SessionDep):
    new_user = crud.create_user(user, session)

    return new_user


@app.get("/users/{user_id}")
async def get_user(user_id: int, session: db.SessionDep):
    user_found = crud.get_user(user_id, session)

    return user_found or {"message": "User not found"}


@app.get("/users")
async def get_users(session: db.SessionDep):
    return crud.get_users(session)


@app.get("/users/{user_id}/accounts")
async def get_accounts_for_user(user_id: int, session: db.SessionDep):
    return crud.get_accounts_for_user(user_id, session)


@app.post("/users/{user_id}/accounts/create")
async def create_account(
    user_id: int, account: schemas.AccountBase, session: db.SessionDep
):
    return crud.create_account(user_id, account, session)


# Sender/receiver id will be another user or id's of accounts for the current user
@app.post("/transactions/create/{sender}/{receiver}")
async def send_money(
    transaction: schemas.TransactionPost, sender, receiver, session: db.SessionDep
):
    return crud.create_transaction(
        sender,
        receiver,
        transaction.created_by,
        transaction.amount,
        transaction.between_user_accounts,
        session,
    )


@app.get("/transactions/{user_id}")
async def get_transactions_for_user(user_id: int, session: db.SessionDep):
    return crud.get_transactions_for_user(user_id, session)


@app.get("/transactions/{user_id}/awaiting_approval")
async def get_transactions_awaiting_approval(user_id: int, session: db.SessionDep):
    return crud.get_transactions_to_approve(user_id, session)


@app.get("/transactions/{transaction_id}/approve")
async def approve_transaction(transaction_id: int, session: db.SessionDep):
    return crud.approve_transaction(transaction_id, session)
