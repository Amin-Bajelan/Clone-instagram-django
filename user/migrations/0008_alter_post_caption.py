# Generated by Django 5.1.6 on 2025-04-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
