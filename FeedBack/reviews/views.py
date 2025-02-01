from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import review
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView

# from .models import review


# Create your views here.
class ReviewView(CreateView):
    model =review
    form_class =ReviewForm
    template_name = "reviews/reviews.html"
    success_url="/Thank-You"


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, "reviews/reviews.html", {"form": form})

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    #         print(form.cleaned_data)

    #         return HttpResponseRedirect("/Thank-You")

    #     return render(request, "reviews/reviews.html", {"form": form})


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


# def ThankYou(request):
#     return render(request, "reviews/Thank_You.html")
# ------------------------------------------
# class ThankYouView(TemplateView):
#     template_name ="Thank_You.html"

# ---------------------------------
# class ThankYouView(View):
#     def get(self,request):
#         return render(request,"reviews/Thank_You.html")
#----0----------------------------------------
class ThankYouView(TemplateView):
    template_name="reviews/Thank_You.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]="hello guys  have a good day"
        return context

class ReviewListView(ListView):
    template_name ="reviews/reviews_list.html"
    model= review
    context_object_name ="reviews"
    
    def get_queryset(self):
        base_Query =  super().get_queryset()
        return base_Query
        

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    reviews =review.objects.all()
    #    context["reviews"] =reviews
    #    return context


        
class AddFavoriteview(View):
        def post(self ,request):
            review_id =request.POST["review_id"]
            #fav_review =  review.objects.get(pk =review_id)
            request.session["favorite_review"] =review_id
            return HttpResponseRedirect("/reviews/"+review_id)

    
class Review_Detail(DetailView):
    template_name = "reviews/review_detail.html"
    model =review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review =self.get_object()
        request =self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] =favorite_id == str(loaded_review.id)
        return context
    


    #  def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)  
    #     review_Id =kwargs["id"]  
    #     selectedReviews =review.objects.get(pk=review_Id)
    #     context["review"] =selectedReviews
    #     return context



