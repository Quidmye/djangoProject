from django.urls import path
from .views import calculate

urlpatterns = [
    path('/<int:first>/<str:operation>/<int:last>', calculate),
]
