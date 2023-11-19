from ast import Div
from bisect import bisect
from email import message
from queue import Empty
from tkinter import EXCEPTION
from tracemalloc import take_snapshot
from turtle import title

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Task, User


def index(request):
    return render(request, "To_do/index.html")

@login_required(login_url='index')
def tasks(request):

    if request.method == "POST":
        task = Task.objects.get(pk=request.POST["task_id"])
        if "done" in request.POST:
            task.is_active = False
            task.save()
        elif "delete" in request.POST: 
            task.delete()
        elif "edit" in request.POST: 
            return HttpResponseRedirect(reverse('edit', args=[str(task.id)]))
    return render(request, "To_do/tasks.html", {"tasks": Task.objects.filter(is_active=True, user=request.user)})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("tasks"))
        else:
            return render(request, "To_do/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "To_do/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "To_do/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "To_do/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "To_do/register.html")

@login_required(login_url='index')
def addtask(request):
    if request.method == "GET":
        return render(request, "To_do/addtask.html")
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        due_date = request.POST["due_date"]
        relevanse = int(request.POST["relev"])
        l = Task(title=name, description=description, due_date = due_date, relevanse =relevanse)
        l.user = request.user
        l.save()
        return HttpResponseRedirect(reverse("tasks"))

@login_required(login_url='index')
def edittask(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        due_date = request.POST["due_date"]
        relevanse = int(request.POST["relev"])

        task.title = name
        task.description = description
        task.due_date = due_date
        task.relevanse = relevanse
        task.save()

        return HttpResponseRedirect(reverse("tasks"))
    return render(request, "To_do/edit.html", {"task": task})




