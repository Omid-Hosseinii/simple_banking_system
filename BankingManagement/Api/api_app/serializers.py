from rest_framework import serializers
from BankingManagement.DB.model import Customer
# from BankingManagement.Process.process import Request


class CustomerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    national_code = serializers.CharField(max_length=10)
    mobile_number = serializers.CharField(max_length=15)
    address = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=100)

class InputSerializer(serializers.Serializer):
    input_data = serializers.CharField()

    def create(self, validated_data):
        # result = Request(validated_data['input_data'])
        result = "sss"
        return result

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['customer_id', 'first_name', 'last_name', 'national_code', 'mobile_number', 'address', 'email']

