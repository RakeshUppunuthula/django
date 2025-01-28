from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
   # path("",views.reviews, name="reviews"),
    path("Thank-You",views.ThankYou,name="Thank-you")
]
