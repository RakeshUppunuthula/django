from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:month>",views.month_Challenges_By_Number),
    path("<str:month>",views.month_Challenges, name = "monthly-challenges")
]



