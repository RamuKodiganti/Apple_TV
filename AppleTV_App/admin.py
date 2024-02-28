from django.contrib import admin

# Register your models here.

from AppleTV_App.models import Student, Branch, Signin, Signup 
#Register models here

admin.site.register(Student)
admin.site.register(Signin)
admin.site.register(Signup)
admin.site.register(Branch)