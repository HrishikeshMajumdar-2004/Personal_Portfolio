from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('projects/',views.projects),
    path('education/',views.education),
    path('experience/',views.experience)
]
