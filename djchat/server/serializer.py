from rest_framework import serializers

from .models import Category, Server # what data to seriealize


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'

