# Generated by Django 4.2.7 on 2023-11-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("To_do", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="task", name="relevanse", field=models.IntegerField(default=1),
        ),
    ]
