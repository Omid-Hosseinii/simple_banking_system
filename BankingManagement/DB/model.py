from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from BankingManagement.DB.connection_db import get_connection
from sqlalchemy.orm import validates

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    national_code = Column(String(10), unique=True, nullable=False)
    mobile_number = Column(String(15), nullable=False)
    address = Column(String(255), nullable=False)
    email = Column(String(100), nullable=True)

    accounts = relationship("Account", back_populates="customer")
    notifications = relationship("Notification", back_populates="customer")

    _locked = False  # برای قفل کردن پس از اولین مقداردهی

    @validates('national_code')
    def validate_national_code(self, key, value):
        if self.national_code is not None and self.national_code != value:
            raise ValueError("national_code cannot be changed once set.")
        return value


class Deposit(Base):
    __tablename__ = 'deposits'

    deposit_id = Column(Integer, primary_key=True, autoincrement=True)
    deposit_type = Column(String(50), nullable=False)
    interest_rate = Column(Float, nullable=False)
    initial_amount = Column(Float, nullable=False)
    maturity_date = Column(DateTime, nullable=True)
    start_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))


class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    creation_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    customer = relationship("Customer", back_populates="accounts")

    sent_transactions = relationship("Transaction", foreign_keys="[Transaction.account_id]",
                                     back_populates="account")
    received_transactions = relationship("Transaction", foreign_keys="[Transaction.destination_account_id]",
                                         back_populates="destination_account")


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(100), nullable=False)
    register_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    status = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)

    account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
    destination_account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=True)

    account = relationship("Account", foreign_keys=[account_id], back_populates="sent_transactions")
    destination_account = relationship("Account", foreign_keys=[destination_account_id],
                                       back_populates="received_transactions")


class Notification(Base):
    __tablename__ = 'notifications'

    notification_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)

    message = Column(String(500), nullable=False)
    notification_type = Column(String(50), nullable=False)
    send_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    customer = relationship("Customer", back_populates="notifications")


Base.metadata.create_all(get_connection())
