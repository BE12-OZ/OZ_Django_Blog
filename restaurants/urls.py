from django.urls import path
from .views import (
    RestaurantListCreateAPIView, 
    RestaurantRetrieveUpdateDestroyAPIView,
    ReviewCreateAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/reviews/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
]
