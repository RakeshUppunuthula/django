from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse




# Create your views here.

Monthly_Challengesc={ "January":"I will complete crash course on django",
"February":"I will complete the Javscript  crash Course",
"March":"I will complete the dsa   crash Course by end",
"April":"I will complete You Practice",
"May":"I will  reduce my body fat by 20 %",
"June":"this is a vacyion month to goa",
"July":"this is nothings",
"August":"this is intresting",
"September":"whtas up",
"October":"How Are You",
"November":"Hi Buddy",
"December":None
}
def index(request):   
    months = list(Monthly_Challengesc.keys())

    return render(request,"challenges/index.html",{"months":months})
    # for month in months:
    #     captilized_month = month.capitalize()
    #     redirect_Path =  reverse("monthly-challenges", args=[month])
    #     list_values+=f"<li><a href=\"{redirect_Path}\">{captilized_month}</a></li>"

    # response_data = f"<ul>{list_values}</ul>" 
    # return HttpResponse(response_data) 







def month_Challenges_By_Number(request ,month):
    months = list(Monthly_Challengesc.keys())
    if month >len(months):
        return HttpResponseNotFound("Invalid Month !")
    forward_Month =months[month-1]
    redirect_Path =  reverse("monthly-challenges", args=[forward_Month])
    return HttpResponseRedirect(redirect_Path)





def month_Challenges(request,month):
    try:
        challenges_Text= Monthly_Challengesc[month]
        return render(request,"challenges/challenge.html",{"text":challenges_Text , "month":month.capitalize()})
        # respose_Text = render_to_string("challenges/challenges.html")
        # #f"<h1>{challenges_Text}</h1>"
        # return HttpResponse(respose_Text)
        
    except: 
         return HttpResponseNotFound("this month is not existed in year  Hahahaha !")
    



