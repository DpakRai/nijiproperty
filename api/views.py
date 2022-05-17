from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from buyproperty.models import House, HouseImage, Comment
from rentproperty.models import Renthouse, Renthouseimage
from sellproperty.models import Sellhouse, Sellhouseimage
from rentproperty.serializers import RenthouseimageSerializer,RenthouseSerializer 
from buyproperty.serializers import HouseImageSerializer,HouseSerializer
from sellproperty.serializers import SellhouseimageSerializer,SellhouseSerializer
#buyproperty 
class Houseinfo(APIView):
    def get(self, request, *args, **kwargs):
        house = House.objects.all()
        print(house[0])
        serializer = HouseSerializer(house, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'House Created Successfully'
        })

class HouseDetail(APIView):
    def put(self, request, pk, *args, **kwargs):
        # Get the Category to update
        house = House.objects.get(pk=pk)

        serializer = HouseSerializer(house,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'House Updated Successfully'
        })

    def delete(self, request, pk, *args, **kwargs):
        house = House.objects.get(pk=pk)

        #delete the Category
        house.delete()
        return Response({
            'message': 'House Deleted Successfully'
        })


class Houseimageinfo(APIView):
    def get(self, request, *args, **kwargs):
        houseimage = HouseImage.objects.all()
        print(houseimage[0])
        serializer = HouseImageSerializer(houseimage, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = HouseImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Houseimage Created Successfully'
        })

#rentproperty
class Renthouseinfo(APIView):
    def get(self, request, *args, **kwargs):
        renthouse = Renthouse.objects.all()
        print(renthouse[0])
        serializer = RenthouseSerializer(renthouse, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RenthouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Rent house Created Successfully'
        })

class RenthouseDetail(APIView):
    def put(self, request, pk, *args, **kwargs):
        # Get the Category to update
        renthouse = Renthouse.objects.get(pk=pk)

        serializer = RenthouseSerializer(renthouse,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Rent house Updated Successfully'
        })

    def delete(self, request, pk, *args, **kwargs):
        renthouse = Renthouse.objects.get(pk=pk)

        #delete the Category
        renthouse.delete()
        return Response({
            'message': 'RentHouse Deleted Successfully'
        })


class Renthouseimageinfo(APIView):
    def get(self, request, *args, **kwargs):
        renthouseimage = Renthouseimage.objects.all()
        print(renthouseimage[0])
        serializer = RenthouseimageSerializer(renthouseimage, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RenthouseimageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Renthouseimage Created Successfully'
        })

#Sellproperty
class Sellhouseinfo(APIView):
    def get(self, request, *args, **kwargs):
        sellhouse = Sellhouse.objects.all()
        print(sellhouse[0])
        serializer = SellhouseSerializer(sellhouse, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SellhouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Sell house Created Successfully'
        })

class SellhouseDetail(APIView):
    def put(self, request, pk, *args, **kwargs):
        # Get the Category to update
        sellhouse = Sellhouse.objects.get(pk=pk)

        serializer = SellhouseSerializer(sellhouse,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Sell house Updated Successfully'
        })

    def delete(self, request, pk, *args, **kwargs):
        sellhouse = Sellhouse.objects.get(pk=pk)

        #delete the Category
        sellhouse.delete()
        return Response({
            'message': 'RentHouse Deleted Successfully'
        })


class Sellhouseimageinfo(APIView):
    def get(self, request, *args, **kwargs):
        sellhouseimage = Sellhouseimage.objects.all()
        print(sellhouseimage[0])
        serializer = SellhouseimageSerializer(sellhouseimage, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SellhouseimageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Sell houseimage Created Successfully'
        })


