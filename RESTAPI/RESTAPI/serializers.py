from rest_framework import serializers
from .models import RESTAPI


class RESTAPISerializer (serializers.ModelSerializer):
    class meta:
        model = RESTAPI
        fields= ['id', 'name', 'desccription']
        