from django.urls import path
from .views import *

urlpatterns = [
    path('',PostList.as_view(), name="index"),
	path('author/',author.as_view(),name="author"),
	path('post/', contact, name="contact"),
	path('single/', single, name="single"),

    path('technology/',TechList.as_view(), name="technology"),
	#path('technology/',technology,name="technology"),
	#path('technology_single/',technology_single,name="technology_single"),
	#path('lifestyle/',LifeList.as_view(), name="lifestyle"),
	#path('lifestyle/',lifestyle,name="lifestyle"),
	#path('life_single/',life_single, name="life_single"),
	path('nature/',natureList.as_view(),name="nature"),
	#path('nature_single/',nature_single,name="nature_single"),
	#path('food/',foodList.as_view(),name="food"),
	#path('food_single/',food_single,name="food_single"),
	path('travel/',travelList.as_view(),name="travel"),
	#path('health/',healthList.as_view(),name="health"),
	path('sports/',sportsList.as_view(), name="sports"),
	path('world/',worldList.as_view(), name="world"),
    path('<int:pk>/',blogpost.as_view(), name="blogpost"),
]