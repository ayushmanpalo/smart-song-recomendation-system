from django.shortcuts import render
from django.urls import path
from iris_app import views

app_name = "iris_app"

urlpatterns = [
    path('', views.predict, name='prediction_page'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
]