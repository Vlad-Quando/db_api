from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .api_db_queryer import get_quantity, get_record_by_id
import json


# Create your views here.
@api_view(['GET'])
def get_quantity_view(request):
    '''Serves quantity/ requests and returns the quantity of records in the table'''

    quantity = get_quantity()[0]
    return Response(data={'Quantity': str(quantity)})


@api_view(['GET'])
def get_record_by_id_view(request, id):
    '''Serves by_id/id=id requests and returns the record with given id or record-not-found error'''

    result = get_record_by_id(id)
    return Response(data=result)