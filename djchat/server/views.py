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
        qty = request.query_params.get("qty")
        # filter by user or not so taken true
        by_user = request.query_params.get("by_user") == "true"

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        if qty:
            self.queryset = self.queryset[: int(qty)]

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
