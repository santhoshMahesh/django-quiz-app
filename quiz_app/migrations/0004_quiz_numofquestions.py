# Generated by Django 4.0 on 2022-07-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_alter_questions_quiz_alter_quiz_quiz_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='numOfQuestions',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
