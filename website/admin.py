from django.contrib import admin
from .models import Slider_Image, Faculty_Member, Floating_image_1, Floating_image_2,  Testomonial, Notice
# Register your models here.

admin.site.register(Slider_Image),
admin.site.register(Faculty_Member),
admin.site.register(Floating_image_1)
admin.site.register(Floating_image_2)
admin.site.register(Testomonial)
admin.site.register(Notice)