
from django import forms
from django.forms import ModelForm

from . import Task


class AddTask(ModelForm):
    class Meta:
        model = Task
        exclude = ["created", "user","is_active"]
  