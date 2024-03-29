# Generated by Django 4.2.4 on 2023-12-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_faculty_member_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floating_image_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='static/floating_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Floating_image_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='static/floating_images/')),
            ],
        ),
    ]
