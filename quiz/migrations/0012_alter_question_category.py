# Generated by Django 4.1.5 on 2023-05-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_remove_quizprofile_bad_performance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Sex Education', 'Sex Education')], max_length=500),
        ),
    ]
