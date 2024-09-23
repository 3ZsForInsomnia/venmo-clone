from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    balance = Column(Integer)
    starting_balance = Column(Integer)

    transactions = relationship("Transaction", back_populates="sender_user")


# Transaction with completed_at == None is a transaction request
# If receiver == None, then it is a withdrawal
# If sender == None, then it is a deposit
# sender is the person sending money to the receiver, regardless of the amount
#   or the creator of the transaction
# E.g., Alice can create a transaction request for $20, with herself as the
#   sender or as the receiver. If she is the receiver, she wants Bob to send
#   her $20, and if she is the sender, she is giving Bob $20.
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(String, index=True)
    amount = Column(Integer)
    sender = Column(Integer, ForeignKey("users.id"), nullable=True)
    reciever = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)
    completed_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime)

    sender_user = relationship("User", back_populates="transactions")
    reciever_user = relationship("User", back_populates="transactions")
    created_by_user = relationship("User", back_populates="transactions")
