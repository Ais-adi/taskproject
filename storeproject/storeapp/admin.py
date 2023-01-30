from django.contrib import admin

# Register your models h
from storeapp.models import Person, Department, Courses
# from storeapp.models import Materials_provide
admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Courses)
# admin.site.register(Materials_provide)

