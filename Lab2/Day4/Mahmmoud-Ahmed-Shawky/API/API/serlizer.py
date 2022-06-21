from rest_framework import routers, serializers, viewsets

from traine.models import *
from users.models import *
class trainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traine
        fields ='__all__'