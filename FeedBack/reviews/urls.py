from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
    #path("Thank-You",ThankYouView.as_view(),name="Thank-you")
    
    path("Thank-You",views.ThankYouView.as_view(),name="Thank-you"),
    path("reviews",views.ReviewListView.as_view()),
    path("reviews/<int:pk>",views.Review_Detail.as_view())
   
   
   # path("",views.reviews, name="reviews"),
    # path("Thank-You",views.ThankYou,name="Thank-you").
]
