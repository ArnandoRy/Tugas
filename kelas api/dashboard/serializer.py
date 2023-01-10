from dashboard.models import asia
from rest_framework import serializers

class asiaSerializer(serializers.ModelSerializer):
    class meta:
        model = asia
        fields = ['nim','nama','sks']