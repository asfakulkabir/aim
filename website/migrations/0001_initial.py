# Generated by Django 4.2.4 on 2023-12-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slider_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silder_title', models.CharField(max_length=300)),
                ('silder_image', models.ImageField(upload_to='static/home_page_images/')),
            ],
        ),
    ]
