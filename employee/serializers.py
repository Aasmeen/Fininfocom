import base64
from rest_framework import serializers

from employee.models import Employee


class Address(serializers.Serializer):
    hno = serializers.CharField()
    street = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()


class CompanyDetails(serializers.Serializer):
    companyName = serializers.CharField()
    fromDate = serializers.CharField()
    toDate = serializers.CharField()
    address = serializers.CharField()


class Qualifications(serializers.Serializer):
    qualificationName = serializers.CharField()
    fromDate = serializers.CharField()
    toDate = serializers.CharField()
    percentage = serializers.FloatField()


class Projects(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()


class EmployeeSerializer(serializers.ModelSerializer):
    addressDetails = Address()
    workExperience = CompanyDetails(many=True)
    qualifications = Qualifications(many=True)
    projects = Projects(many=True)

    class Meta:
        model = Employee
        fields = '__all__'

