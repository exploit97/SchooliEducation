from django.contrib import admin
from .models import Evaluation, Category, Solution, Subject,Matter,Level,Country,Etablissement,Year,SubCategory

# Register your models here.




admin.site.register(Subject)
admin.site.register(Evaluation)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Solution)
admin.site.register(Level)
admin.site.register(Country)
admin.site.register(Matter)
admin.site.register(Etablissement)
admin.site.register(Year)

