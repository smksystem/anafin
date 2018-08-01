from django.contrib import admin

# Register your models here.

from .models import anaform
class anaformAdmin (admin.ModelAdmin):
	list_display = ['__unicode__','email','timestamp','updated']
	class Meta:
		model= anaform

admin.site.register(anaform,anaformAdmin)
