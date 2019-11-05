from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from django.http import HttpResponse
from prices.models import Price, MDPrice
from prices import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class PricesListView(ListCreateAPIView):

    serializer_class = serializers.PriceSerializer
    permission_classes = tuple()
    queryset = Price.objects.all().order_by("id")


class PriceDetailView(RetrieveUpdateAPIView):
    serializer_class = serializers.PriceSerializer
    permission_classes = tuple()
    queryset = Price.objects.all().order_by("id")


class MDPricesListView(ListCreateAPIView):
    serializer_class = serializers.MDPriceSerializer

    def get_queryset(self):
        queryset = MDPrice.objects.all()
        return queryset


class MDPriceDetailView(RetrieveUpdateAPIView):
    serializer_class = serializers.MDPriceSerializer
    permission_classes = tuple()

    def get_queryset(self):
        queryset = MDPrice.objects.all()
        return queryset
