from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at leat 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at leat 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at leat 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at leat 20 minutes every day!", 
}
# Create your views here.

def index(request):
    list_items = ""

    months = list(challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return HttpResponse("Learn Django for at leat 20 minutes every day!")
## Dynamic view
def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month = months[month - 1]
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    redirect_path =  reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


## before dictionary

# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = "Eat no meat for the entire month!"
#     elif month == 'february':
#         challenge_text = "Walk for at least 20 minutes every day!"
#     elif month == 'march':
#         challenge_text = "Learn Django for at leat 20 minutes every day!"
#     else:
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(challenge_text)

## After dictionary
def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # return HttpResponse(challenge_text)
        ## response_data= render_to_string("challenges/challenge.html")
        ## return HttpResponse(response_data)
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
            # "month_name": month.capitalize()
        })
        
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")