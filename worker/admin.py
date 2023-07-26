from django.contrib import admin
from .models import Workers
from  .models import Coment
from .models import Resume

# Register your models here.
admin.site.register(Workers)
admin.site.register(Coment)
admin.site.register(Resume)
