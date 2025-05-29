from typing import Dict
from BankingManagement.DB.model import Customer
from BankingManagement.DB.get_session import get_session


class CustomerManager:
    def __init__(self, customer_info: Dict):
        self.customer_info = customer_info




class CustomerCreate(CustomerManager):
    def save_db(self):
        session = get_session()

        new_customer = Customer(first_name=self.customer_info.get('first_name'),
                                last_name=self.customer_info.get('last_name'),
                                national_code=self.customer_info.get('national_code'),
                                mobile_number=self.customer_info.get('mobile_number'),
                                address=self.customer_info.get('address'),
                                email=self.customer_info.get('email'))

        session.add(new_customer)
        session.commit()

        return True