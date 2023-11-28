from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError

from employee.serializers import EmployeeSerializer 
from employee.models import Employee

class EmployeeAPIViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def filter_queryset(self, queryset):
        if self.request.query_params.get('regid'):
            empId = ''.join(filter(str.isdigit, self.request.query_params['regid']))
            queryset = queryset.filter(id=int(empId))
        elif self.kwargs.get('pk'):
            self.kwargs['pk'] = int(''.join(filter(str.isdigit, self.kwargs['pk'])))
        return queryset

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            response_data = {
                "message": "employee details found",
                "employees": serializer.data,
                "sucess": True
            }
        except Http404 as e:
            response_data = {
                "message": "employee details not found",
                "employees": [],
                "sucess": False
            }
        except Exception as e:
            response_data = {
                "message": "employee data failed",
                "success": False
            }
        return Response(response_data)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "message": "employee details found",
                "employees": serializer.data,
                "sucess": True
            }
        except Http404 as e:
            response_data = {
                "message": "employee details not found",
                "employees": [],
                "sucess": False
            }
        except Exception as e:
            response_data = {
                "message": "employee data failed",
                "success": False
            }
        return Response(response_data)

    def update(self, request, *args, **kwargs):
        try:
            super().update(request,*args,**kwargs)
            response_data = {
                "message": "employee updated successfully",
                "success": True
            }
            status_code = status.HTTP_200_OK
        except ValidationError as e:
            for field, error_details in e.detail.items():
                for error_detail in error_details:
                    if error_detail.code == 'required':
                        response_data = {
                            "message": "invalid body request",
                            "sucess": False
                        }
                        status_code = status.HTTP_400_BAD_REQUEST
                        break
                if response_data:
                    break
        except Http404 as e:
            response_data = {
                "message": "employee updation failed",
                "success": False
            }
            status_code = status.HTTP_200_OK
        except Exception as e:
            response_data = {
                "message": "employee updation failed",
                "success": False
            }
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_data, status=status_code)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request,*args,**kwargs)
            response_data = {
                "message": "employee deleted successfully",
                "success": True
            }
            status_code = status.HTTP_200_OK
        except Http404 as e:
            response_data = {
                "message": "employee deletion failed",
                "success": False
            }
            status_code = status.HTTP_200_OK
        except Exception as e:
            response_data = {
                "message": "employee deletion failed",
                "success": False
            }
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_data, status=status_code)

    def create(self, request, *args, **kwargs):
        response_data = {}
        try:
            reponse = super().create(request, *args, **kwargs)
            response_data = {
                "message": "employee created successfully",
                "regid": "EMP" + str(reponse.data['id']),
                "sucess": True
            }
        except ValidationError as e:
            for field, error_details in e.detail.items():
                for error_detail in error_details:
                    if error_detail.code == 'unique':
                        response_data = {
                            "message": "employee already exist",
                            "sucess": False
                        }
                        break
                    elif error_detail.code == 'required':
                        response_data = {
                            "message": "invalid body request",
                            "sucess": False
                        }
                        break
                if response_data:
                    break
        except Exception as e:
            response_data = {
                "message": "employee created failed",
                "success": False
            }
        return Response(response_data, status=status.HTTP_201_CREATED)