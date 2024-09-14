from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import UserCard, Skill

class User_cardAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram_id', 'grade')
    list_filter = ('grade', 'user')
    search_fields = ('user', 'telegram_id')

    fieldsets = (
        ('User Credentials', {'fields': ('user', 'telegram_id')}),
        ('Personal info', {'fields': ('country', 'city', 'description')}),
        ('Pofessional info', {'fields': ('grade', 'skills_user')}),
    )

    def save_model(self, request, obj, form, change):
        if obj.user_id is None:
            obj.user_id = request.user.id

        # if obj.id is None:
        #     obj.id = 90
        # if obj.skills_user.count() < 3:
        #     print(obj.skills_user.count())
        #     raise ValidationError("Please add at least 3 skills")

        super().save_model(request, obj, form, change)

class skillsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'slug')

admin.site.register(UserCard, User_cardAdmin)
admin.site.register(Skill, skillsAdmin)
