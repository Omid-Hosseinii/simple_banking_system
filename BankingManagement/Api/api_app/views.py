from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer
from BankingManagement.Process.Customer.customer_process import CustomerQuery, CustomerCreate
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome to the homepage!</h1>")


class DataAPIView(APIView):
    def get(self, request):
        customer_query = CustomerQuery()
        customers = customer_query.find_all()
        serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer_info= {
                        'first_name': serializer.validated_data['first_name'],
                        'last_name' : serializer.validated_data['last_name'],
                        'national_code' : serializer.validated_data['national_code'],
                        'mobile_number' : serializer.validated_data['mobile_number'],
                        'address' : serializer.validated_data['address'],
                        'email' : serializer.validated_data['email']}

            create_customer = CustomerCreate(customer_info).save_db()
            if create_customer:
                return Response({"status": "success", "description": "The customer has been created!"})

        return Response(serializer.errors, status=400)
