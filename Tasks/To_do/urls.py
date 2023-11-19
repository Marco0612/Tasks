from pydoc import visiblename

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addtask", views.addtask, name="addtask"),
    path("tasks", views.tasks, name="tasks"),
    path("edit/<int:task_id>", views.edittask, name="edit")
]
