from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Server
from .serializer import ServerSerializer

# Create your views here.

# child class of viewset


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()  # returns all the servers

    def list(self, request):

        # parse the category id from request
        category = request.query_params.get("category")

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
