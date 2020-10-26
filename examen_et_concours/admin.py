from django.contrib import admin
from .models import Concours, Category, Solution, Subject,Matter,Level,Country,Etablissement,Year

# Register your models here.




admin.site.register(Subject)
admin.site.register(Concours)
admin.site.register(Category)
admin.site.register(Solution)
admin.site.register(Level)
admin.site.register(Country)
admin.site.register(Matter)
admin.site.register(Etablissement)
admin.site.register(Year)

