from django.contrib import admin
from mainapp.models import hydrabad,goa,noida,meerut
# Register your models here.
class hydrabad_admin(admin.ModelAdmin):
    #title qualification address date contact
    list_display=['title','qualification','address','date','contact']
admin.site.register(hydrabad,hydrabad_admin)

class goa_admin(admin.ModelAdmin):
    #title qualification address date contact
    list_display=['title','qualification','address','date','contact']
admin.site.register(goa,goa_admin)


class noida_admin(admin.ModelAdmin):
    #title qualification address date contact
    list_display=['title','qualification','address','date','contact']
admin.site.register(noida,noida_admin)

class meerut_admin(admin.ModelAdmin):
    #title qualification address date contact
    list_display=['title','qualification','address','date','contact']
admin.site.register(meerut,meerut_admin)