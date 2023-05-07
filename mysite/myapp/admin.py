from django.contrib import admin
from myapp.models import People,Article,Comment,UserProfile

# Register your models here.
admin.site.register(People)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserProfile)
