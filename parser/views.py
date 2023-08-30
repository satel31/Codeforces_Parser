from rest_framework import generics

from parser.models import Problem
from parser.serializers import ProblemCreateSerializer, ProblemListSerializer, ProblemDetailSerializer


class ProblemCreateAPIView(generics.CreateAPIView):
    """View to create a habit."""
    serializer_class = ProblemCreateSerializer


class ProblemListAPIView(generics.ListAPIView):
    """View to get a list of habits (returns only your own habits)."""
    serializer_class = ProblemListSerializer
    queryset = Problem.objects.all()


class ProblemDetailAPIView(generics.RetrieveAPIView):
    """View to get a particular habit by its id (returns only your own habits).
       In case of the tests don't forget to change permissions."""
    serializer_class = ProblemDetailSerializer
    queryset = Problem.objects.all()
