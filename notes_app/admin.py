from django.contrib import admin
from .models import Notes
# Register your models here.


admin.site.site_header='Admin Panel'
admin.site.site_title='Admin Panel'

admin.site.site_index='Admin Panel'

admin.site.register(Notes)
