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
    list_display = ('id', 'last_name', 'first_name', 'department', 'is_submitted', 'issue_toll_card', 'training', 'share_personal_email', 'post_photo_video_audio', 'voluntary_activity', 'corporate_assets', 'discount_card')
    inlines = [PersonnelOptionsAdminInline, ]

    def is_submitted(self, x):
        return bool(x.personnel_options.is_submitted)
    is_submitted.short_description = 'Is submitted?'
    is_submitted.boolean = True

    def issue_toll_card(self, x):
        return bool(x.personnel_options.issue_toll_card)
    issue_toll_card.short_description = 'Issue Toll Card'
    issue_toll_card.boolean = True

    def training(self, x):
        return bool(x.personnel_options.training)
    training.short_description = 'Training'
    training.boolean = True

    def share_personal_email(self, x):
        return bool(x.personnel_options.share_personal_email)
    share_personal_email.short_description = 'Share Personal Email'
    share_personal_email.boolean = True

    def post_photo_video_audio(self, x):
        return bool(x.personnel_options.post_photo_video_audio)
    post_photo_video_audio.short_description = 'Photo/Video/Audio Post'
    post_photo_video_audio.boolean = True

    def voluntary_activity(self, x):
        return bool(x.personnel_options.voluntary_activity)
    voluntary_activity.short_description = 'Voluntary Activity'
    voluntary_activity.boolean = True

    def corporate_assets(self, x):
        return bool(x.personnel_options.corporate_assets)
    corporate_assets.short_description = 'Corporate Assets'
    corporate_assets.boolean = True

    def discount_card(self, x):
        return bool(x.personnel_options.discount_card)
    discount_card.short_description = 'Discount Card'
    discount_card.boolean = True