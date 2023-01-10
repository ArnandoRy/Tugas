from dashboard.models import asia
from dashboard.serializer import asiaSerializer
from rest_framework import viewsets

class asiaViewset(viewsets.ModelViewSet):
    queryset = asia.objects.all()
    serializer_class = asiaSerializer