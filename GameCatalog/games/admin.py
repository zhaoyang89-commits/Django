from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Developer
from .models import Platform
from .models import Game
from .models import GameDetail

admin.site.register(Developer)
admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(GameDetail)