from django.contrib import admin

from personnel.models import Department, ConsentForm, PersonnelOptions

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('name',)

class PersonnelOptionsAdminInline(admin.StackedInline):
    model = PersonnelOptions
    exclude = ()

@admin.register(ConsentForm)
class ConsentFormAdmin(admin.ModelAdmin):
    model = ConsentForm
    exclude = ()
    inlines = [PersonnelOptionsAdminInline,]
