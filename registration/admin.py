from django.contrib import admin
from .models import Specialisation, Doctor, Term, Complaint
# Register your models here.

admin.site.register(Specialisation)
admin.site.register(Doctor)
admin.site.register(Term)
admin.site.register(Complaint)