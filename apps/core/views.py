from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item


def home(request):
    items = Item.objects.all()
    return render(
        request,
        "core/home.html",
        {
            "title": "Home",
            "content": "Welcome to the home page",
            "year": datetime.now().year,
            "items": items
        }
    )



def add_item(request):
    if request.method == "POST":
        name = request.POST.get("item-name")
        # Item.objects.create(name=name)
        item = Item(name=name)
        item.save()
        # flash message
        messages.add_message(
            request,
            messages.SUCCESS,
            "Item added successfully"
        )

        return HttpResponse(f"<li> {item.name} </li>")
    return redirect("core:home")