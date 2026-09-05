from django.shortcuts import render


items = [
    {"name": "Finish homework", "completed": True},
    {"name": "Study for accounting", "completed": False},
    {"name": "Go to the gym", "completed": True},
    {"name": "Update my resume", "completed": False},
    {"name": "Apply for internships", "completed": False},
]


def home(request):
    return render(request, "home.html", {"items": items})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")