from django.contrib import admin

from app.models import CustomUser, Vacation

# Register your models here.
admin.site.register(CustomUser)


def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]



class VacationAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Vacation)
    # search_fields=["start_at"]
    list_filter = ['employee',"start_at","end_at"]


admin.site.register(Vacation, VacationAdmin)

