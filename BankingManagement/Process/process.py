from enum import Enum
from typing import Dict, Optional
from Process.Customer.customer_process import CustomerCreate



class RequestTypeEnum(Enum):
    CREATECUSTOMER = "create_customer"
    UPDATECUSTOMER = "update_customer"
    OPENDEPOSIT = "open_deposit"
    CREATEACCOUNT = "create_account"
    BALANCEACCOUNT = "get_balance_account"
    BILLACCOUNT = "get_bill_account"
    TRANSFER = "transfer"



class Request:
    def __init__(self, request_type: RequestTypeEnum, json_data: Dict):
        self.request_type = request_type
        self.json_data = json_data

    def __repr__(self):
        return str(self.json_data), str(self.request_type)



class RequestHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler
        return next_handler


    def handle(self, request: Request):
        if self.next_handler:
            return self.next_handler.handle(request)
        else:
            print("This Request is not available")


class CustomerCreateHandler(RequestHandler):
    def handle(self, request: Request):
        if request.request_type == RequestTypeEnum.CREATECUSTOMER.value:
            status = CustomerCreate(request.json_data).save_db()
            if status:
                print("Customer Created successfully")
        else:
            super().handle(request)


class UpdateCustomerHandler(RequestHandler):
    def handle(self, request: Request):
        if request.request_type == RequestTypeEnum.UPDATECUSTOMER.value:
            ...
        else:
            super().handle(request)


class OpenDepositHandler(RequestHandler):
    def handle(self, request: Request):
        if request.request_type == RequestTypeEnum.OPENDEPOSIT.value:
            ...
        else:
            super().handle(request)


class CreateAccountHandler(RequestHandler):
    def handle(self, request: Request):
        if request.request_type == RequestTypeEnum.CREATEACCOUNT.value:
            ...
        else:
            super().handle(request)


class BalanceAccountHandler(RequestHandler):
    def handle(self, request: Request):
        if request.request_type == RequestTypeEnum.BALANCEACCOUNT.value:
            ...
        else:
            super().handle(request)


class BillAccountHandler(RequestHandler):
    def handle(self, request: Request):
        if request.request_type == RequestTypeEnum.BILLACCOUNT.value:
            ...
        else:
            super().handle(request)


class TransferHandler(RequestHandler):
    def handle(self, request: Request):
        if request.request_type == RequestTypeEnum.TRANSFER.value:
            ...
        else:
            super().handle(request)




# customer_create = CustomerCreateHandler()
# update_customer = UpdateCustomerHandler()
# open_deposit = OpenDepositHandler()
# create_account = CreateAccountHandler()
# balance_account = BalanceAccountHandler()
# bill_account = BillAccountHandler()
# transfer = TransferHandler()
#
# (customer_create.set_next_handler(update_customer).
#  set_next_handler(open_deposit).set_next_handler(create_account).set_next_handler(bill_account).
#  set_next_handler(balance_account).set_next_handler(transfer))
#
#
#
# request_ = Request("create_customer", {'first_name': 'Mohammad', "last_name": "Mohammadi",
#                                       "national_code": '1224563890', "mobile_number": '09120233117',
#                                       "address": 'Tehran, Sattarkhan St.', "email":"m.mohammadi@example.com"})
#
# customer_create.handle(request_)