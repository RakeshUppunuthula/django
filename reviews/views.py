from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View

# from .models import review


# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/reviews.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()

            print(form.cleaned_data)

            return HttpResponseRedirect("/Thank-You")

        return render(request, "reviews/reviews.html", {"form": form})


# def reviews(request):

#     if request.method == "POST":
#        #existing_model =review.objects.get(pk=1)  #--- updating Existing Data for updating
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # review_data = review(
#             #     user_Name=form.cleaned_data["user_Name"],
#             #     review_Text=form.cleaned_data["review_Text"],
#             #     rating=form.cleaned_data["rating"],
#             # )
#             #review_data.save()

#             print(form.cleaned_data)
#             # enetered_Username =request.POST['username']
#             # if enetered_Username=="" :
#             # return render(request, "reviews/reviews.html" ,{"has_error":True})

#             # print(enetered_Username)

#             return HttpResponseRedirect("/Thank-You")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/reviews.html", {"form": form})


def ThankYou(request):
    return render(request, "reviews/Thank_You.html")
