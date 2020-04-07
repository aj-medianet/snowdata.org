from rest_framework import generics
from app.models import SkiArea
from .serializers import SkiAreaSerializer

class SkiAreaRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = SkiAreaSerializer