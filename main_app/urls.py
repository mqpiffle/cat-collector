from django.urls import path
from . import views

urlpatterns = [
    # using an '' makes this our root route
    # views.home refers to a view which renders a file
    # and the name='home kwarg gives the route a name
    # naming routes is optional but best practice
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index')
]