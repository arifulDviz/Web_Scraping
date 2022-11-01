import csv
import json
from django.http import StreamingHttpResponse
from django.shortcuts import render
from rest_framework import response
from .models import Bilbasen_data, Biltorvet_data

from rest_framework.decorators import api_view, renderer_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.settings import api_settings
from rest_framework_csv import renderers
from rest_framework import status
from rest_framework_csv.renderers import CSVRenderer

from .serializers import Bilbasen_dataSerializer, Biltorvet_dataSerializer

# Create your views here.


@csrf_exempt
@api_view(['GET'])
def Populating_Bilbasen_data_To_Database(request):
    Bilbasen_file = open(
        './scrapper/Bilbasen/bilbasen_data.json', 'r', encoding="utf8")
    Bilbasen_data.objects.all().delete()
    Bilbasen_data_json = json.loads(Bilbasen_file.read())
    for data in Bilbasen_data_json:
        temp_data = Bilbasen_data(
        )
        temp_data.Name = data['Name']
        temp_data.Address = data['Address']
        temp_data.Phone = data['Phone']
        temp_data.Fax = data['Fax']
        temp_data.Number_of_listings = data['Number_of_listings']
        temp_data.Web_Link = data['Web_Link']

        temp_data.save()

        print(data)
    return Response(Bilbasen_data.objects.all().values())


@csrf_exempt
@api_view(['GET'])
def Populating_Biltorvet_data_To_Database(request):
    Biltorvet_file = open(
        './scrapper/Biltorvet/biltorvet_data.json', 'r', encoding="utf8")
    Biltorvet_data.objects.all().delete()
    Biltorvet_data_json = json.loads(Biltorvet_file.read())
    for data in Biltorvet_data_json:
        temp_data = Biltorvet_data()

        temp_data.id = data['id']
        temp_data.name = data['name']
        temp_data.address = data['address']
        temp_data.zipAndCity = data['zipAndCity']
        temp_data.website = data['website']
        temp_data.phone = data['phone']
        temp_data.adCount = data['adCount']
        # temp_data.Web_Link = data['Web_Link']

        temp_data.save()

        print(data)
    return Response(Biltorvet_data.objects.all().values())

    pass


class Bilbasen_dataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bilbasen_data.objects.all()
    serializer_class = Bilbasen_dataSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Biltorvet_dataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Biltorvet_data.objects.all()
    serializer_class = Biltorvet_dataSerializer


@csrf_exempt
@api_view(['GET'])
@renderer_classes((CSVRenderer,))
def Bilbasen_data_CSV(request):

    Bilbasen_data_serializer = Bilbasen_dataSerializer(
        Bilbasen_data.objects.all(), many=True)

    return Response(Bilbasen_data_serializer.data)


@csrf_exempt
@api_view(['GET'])
@renderer_classes((CSVRenderer,))
def Biltorvet_data_CSV(request):

    Biltorvet_data_serializer = Biltorvet_dataSerializer(
        Biltorvet_data.objects.all(), many=True)

    return Response(Biltorvet_data_serializer.data)
