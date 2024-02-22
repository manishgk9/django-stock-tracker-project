from django.urls import path
from app import views
urlpatterns = [
    path('', views.stockPiker, name='stockPiker'),
    path('stockTracker/', views.stockTracker, name='stockTracker')
]
