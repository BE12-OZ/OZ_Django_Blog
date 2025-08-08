from django.urls import path
from .views import (
    RestaurantListCreateAPIView, 
    RestaurantRetrieveUpdateDestroyAPIView,
    ReviewCreateAPIView
)

urlpatterns = [
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/reviews/', ReviewCreateAPIView.as_view(), name='review-create'),
]
