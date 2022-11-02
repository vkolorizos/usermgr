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
    list_display = ('id', 'last_name', 'first_name', 'department', 'is_submitted', 'issue_toll_card', 'training')
    inlines = [PersonnelOptionsAdminInline, ]

    def issue_toll_card(self, x):
        return bool(x.personnel_options.issue_toll_card)
    issue_toll_card.short_description = 'Issue Toll Card'
    issue_toll_card.boolean = True

    def training(self, x):
        return bool(x.personnel_options.training)
    training.short_description = 'Training'
    training.boolean = True