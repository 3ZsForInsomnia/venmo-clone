from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        username=user.username,
        hashed_password=fake_hashed_password,
        starting_balance=user.starting_balance,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_transactions_for_user(db: Session, user: schemas.User):
    return (
        db.query(models.Transaction).filter(models.Transaction.sender == user.id).all()
        + db.query(models.Transaction)
        .filter(models.Transaction.reciever == user.id)
        .all()
    )


def get_deposits_for_user(db: Session, user: schemas.User):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.reciever == user.id)
        .all()
    )


def get_withdrawals_for_user(db: Session, user: schemas.User):
    return (
        db.query(models.Transaction).filter(models.Transaction.sender == user.id).all()
    )


def get_pending_transactions_for_user(db: Session, user: schemas.User):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.sender == user.id)
        .filter(models.Transaction.reciever == None)
        .all()
        + db.query(models.Transaction)
        .filter(models.Transaction.reciever == user.id)
        .filter(models.Transaction.sender == None)
        .all()
    )


def get_completed_transactions_for_user(db: Session, user: schemas.User):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.sender == user.id)
        .filter(models.Transaction.reciever != None)
        .all()
        + db.query(models.Transaction)
        .filter(models.Transaction.reciever == user.id)
        .filter(models.Transaction.sender != None)
        .all()
    )


def get_deposits_and_withdrawals_for_user(db: Session, user: schemas.User):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.sender == user.id)
        .filter(models.Transaction.reciever == None)
        .all()
        + db.query(models.Transaction)
        .filter(models.Transaction.reciever == user.id)
        .filter(models.Transaction.sender == None)
        .all()
    )


def create_deposit(
    db: Session, user: schemas.User, transaction: schemas.TransactionBase
):
    db_transaction = models.Transaction(
        amount=transaction.amount,
        sender=None,
        reciever=user.id,
        note=transaction.note,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def create_withdrawal(
    db: Session, user: schemas.User, transaction: schemas.TransactionBase
):
    db_transaction = models.Transaction(
        amount=transaction.amount,
        sender=user.id,
        reciever=None,
        note=transaction.note,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def create_request(db: Session, transaction: schemas.TransactionBase):
    db_request = models.Transaction(
        amount=transaction.amount,
        sender=transaction.sender,
        reciever=transaction.receiver,
        note=transaction.note,
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def create_payment(
    db: Session,
    transaction: schemas.Transaction,
):
    db_payment = models.Transaction(
        amount=transaction.amount,
        sender=transaction.sender,
        reciever=transaction.receiver,
        note=transaction.note,
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def get_transaction(db: Session, transaction_id: int):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.id == transaction_id)
        .first()
    )
