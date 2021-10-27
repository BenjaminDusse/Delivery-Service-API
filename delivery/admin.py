from django.contrib import admin
from .models import Branch, Status, Order, User

admin.site.register(Branch)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(User)
