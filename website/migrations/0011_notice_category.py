# Generated by Django 4.2.4 on 2023-12-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='category',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]