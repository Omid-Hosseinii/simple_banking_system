from sqlalchemy.orm import sessionmaker
from BankingManagement.DB.connection_db import get_connection
from BankingManagement.DB.model import Customer


engine = get_connection()

Session = sessionmaker(bind=engine)
session = Session()

# new_customer = Customer(
#     first_name='Ali',
#     last_name='Ahmadi',
#     national_code='1234567890',
#     mobile_number='09121234567',
#     address='Tehran, Enghelab St.',
#     email='ali@example.com'
# )
#
# session.add(new_customer)
# session.commit()
#
# print("مشتری با موفقیت اضافه شد.")



customers = session.query(Customer).all()
customer = session.query(Customer).filter_by(national_code='1234567890').first()
print(customer.first_name)