# Generated by Django 4.1.5 on 2023-05-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_alter_category_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[], max_length=500),
        ),
    ]
