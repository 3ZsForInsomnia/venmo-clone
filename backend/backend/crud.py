from datetime import datetime

from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from . import models, schemas


def login(username: str, password: str, db: Session):
    statement = select(models.User).where(
        models.User.username == username, models.User.password == password
    )
    found_user = db.exec(statement).first()

    if not found_user:
        raise HTTPException(status_code=404, detail="User not found")

    accounts = get_accounts_for_user(found_user.id or 0, db)

    if not accounts:
        raise HTTPException(status_code=422, detail="User has no accounts")

    return schemas.UserLoginResponse(
        user=schemas.User(**found_user.__dict__),
        accounts=[schemas.Account(**account.__dict__) for account in accounts],
    )


def create_user(user: schemas.UserCreate, db: Session):
    statement = select(models.User).where(models.User.username == user.username)
    found_user = db.exec(statement).first()

    if found_user:
        raise HTTPException(status_code=422, detail="Username already exists")

    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    user_response = schemas.User(**db_user.__dict__)

    db_account = models.Account(
        name=user.first_account_name,
        balance=user.starting_balance,
        is_primary=True,
        user_id=db_user.id,
    )

    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return schemas.UserLoginResponse(
        user=user_response,
        accounts=[schemas.Account(**db_account.__dict__)],
    )


def get_user(user_id: int, db: Session):
    return db.get(models.User, user_id)


def get_users(db: Session):
    statement = select(models.User)

    return db.exec(statement).all()


def get_accounts_for_user(user_id: int, db: Session):
    statement = select(models.Account).where(models.Account.user_id == user_id)

    return db.exec(statement).all()


def create_account(user_id: int, account: schemas.AccountBase, db: Session):
    db_account = models.Account(
        name=account.name, balance=account.balance, user_id=user_id
    )

    db.add(db_account)

    db.commit()
    db.refresh(db_account)

    return db_account


def create_transaction(
    sender_id: int,
    receiver_id: int,
    creator: int,
    amount: int,
    between_user_accounts,
    db: Session,
):
    current_time = datetime.now()
    approved = between_user_accounts or False

    db_transaction = models.Transaction(
        sender=sender_id,
        receiver=receiver_id,
        created_by=creator,
        amount=amount,
        created_at=current_time,
        approved=approved,
    )

    db.add(db_transaction)

    db.commit()
    db.refresh(db_transaction)

    return db_transaction


def get_transaction(transaction_id: int, db: Session):
    return db.get(models.Transaction, transaction_id)


def get_transactions_for_user(user_id: int, db: Session):
    statement = (
        select(models.Transaction)
        .where(models.Transaction.sender == user_id)
        .where(models.Transaction.receiver == user_id)
        .where(models.Transaction.created_by == user_id)
    )
    return db.exec(statement).all()


def get_transactions_to_approve(user_id: int, db: Session):
    statement = select(models.Transaction).where(
        models.Transaction.receiver == user_id, models.Transaction.approved == False
    )
    return db.exec(statement).all()


def approve_transaction(transaction_id: int, db: Session):
    db_transaction = db.get(models.Transaction, transaction_id)

    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    if db_transaction.approved:
        raise HTTPException(status_code=422, detail="Transaction already approved")

    db_transaction.approved = True
    db_transaction.approved_on = datetime.now()

    db.commit()
    db.refresh(db_transaction)

    return db_transaction
