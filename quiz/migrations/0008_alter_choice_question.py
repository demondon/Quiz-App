# Generated by Django 4.1.5 on 2023-05-06 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_remove_quizquestion_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.question'),
        ),
    ]
