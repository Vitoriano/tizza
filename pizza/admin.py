from django.contrib import admin

from pizza.models import Pizza, Pizzeria, Likes

admin.site.register(Pizzeria)
admin.site.register(Pizza)
admin.site.register(Likes)
