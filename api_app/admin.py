from django.contrib import admin
from .models import Product, MSO, Doctor, ARC, HQ, Chemist
# Register your models here.


admin.site.register(Product)
admin.site.register(MSO)
admin.site.register(Doctor)
admin.site.register(ARC)
admin.site.register(HQ)
admin.site.register(Chemist)


