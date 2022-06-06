from django.urls import path
from .views import *


urlpatterns = [
    path('', ListProductVIew.as_view()),
    path('<int:pk>/', RetrieveProductVIew.as_view()),
    path('create/', CreateProductVIew.as_view()),
    path('delete/<int:pk>/', DestroyProductVIew.as_view()),
    path('update/<int:pk>/', UpdateProductVIew.as_view()),
    path('page/', ListProductVIew.as_view()),
]