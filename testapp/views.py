from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .quicksort import quick_sort


# CREATE + GET ALL
@api_view(['GET', 'POST'])
def user_list(request):

    # CREATE
    if request.method == 'POST':

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    # GET ALL
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


# GET SINGLE + UPDATE + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):

    user = User.objects.get(id=id)

    # GET SINGLE
    if request.method == 'GET':

        serializer = UserSerializer(user)

        return Response(serializer.data)

    # UPDATE
    elif request.method == 'PUT':

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    # DELETE
    elif request.method == 'DELETE':

        user.delete()

        return Response({
            "message": "User Deleted"
        })


# QUICK SORT API
@api_view(['GET'])
def sorted_users(request):

    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    sorted_data = quick_sort(serializer.data)

    return Response(sorted_data)

# Create your views here.
