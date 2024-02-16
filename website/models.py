from django.db import models
from ckeditor.fields import RichTextField


class Slider_Image(models.Model):
    slider_title= models.CharField(max_length=300)
    slider_image = models. ImageField(upload_to='static/home_page_images/',blank=False)

    def __str__(self):
        return self.slider_title


class Faculty_Member(models.Model):
    tecaher_name= models.CharField(max_length=300)
    tecaher_rank= models.CharField(max_length=300)
    studied_subject= models.CharField(max_length=300)
    institute= models.CharField(max_length=300)
    description= models.CharField(max_length=300, blank=True)
    teacher_image = models. ImageField(upload_to='static/teacher_images/',blank=False)

    def __str__(self):
        return self.tecaher_rank

class Floating_image_1(models.Model):
    title= models.CharField(max_length=300)
    description= models.CharField(max_length=1000)
    image = models. ImageField(upload_to='static/floating_images/',blank=False)

    def __str__(self):
        return self.title

class Floating_image_2(models.Model):
    title= models.CharField(max_length=300)
    description= models.CharField(max_length=1000)
    image = models. ImageField(upload_to='static/floating_images/',blank=False)

    def __str__(self):
        return self.title
        
class Testomonial(models.Model):
    name= models.CharField(max_length=300)
    identity= models.CharField(max_length=300)
    description= models.TextField(max_length=200)

    def __str__(self):
        return self.name


# notices 
class Notice(models.Model):
    notice_name= models.CharField(max_length=300)
    category= models.CharField(max_length=300, blank=True)
    upload_at= models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='static/notice_pdf/', blank=False)

    def __str__(self):
        return self.notice_name