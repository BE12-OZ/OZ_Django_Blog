from rest_framework import generics
from .models import Restaurant, Review
from .serializers import RestaurantSerializer, ReviewSerializer

class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        serializer.save(restaurant=restaurant)