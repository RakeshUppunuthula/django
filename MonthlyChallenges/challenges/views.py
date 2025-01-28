from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

Monthly_Challengesc = {
    "January": "I will complete crash course on django",
    "February": "I will complete the Javscript  crash Course",
    "March": "I will complete the dsa   crash Course by end",
    "April": "I will complete You Practice",
    "May": "I will  reduce my body fat by 20 %",
    "June": "this is a vacyion month to goa",
    "July": "this is nothings",
    "August": "this is intresting",
    "September": "whtas up",
    "October": "How Are You",
    "November": "Hi Buddy",
    "December": None,
}

def index(request):
    months = list(Monthly_Challengesc.keys())

    return render(request, "challenges/index.html", {"months": months})
 
def month_Challenges_By_Number(request, month):
    months = list(Monthly_Challengesc.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month !")
    forward_Month = months[month - 1]
    redirect_Path = reverse("monthly-challenges", args=[forward_Month])
    return HttpResponseRedirect(redirect_Path)

def month_Challenges(request, month):
    try:
        challenges_Text = Monthly_Challengesc[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenges_Text, "month": month.capitalize()},
        )
    except:
        raise Http404()
