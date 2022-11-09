from django.db import models

issubmitted_choice = (
    ('Not delivered yet', 'Not delivered yet'),
    ('Yes', 'Yes'),
    ('maternity leave', 'maternity leave'),
)


class Department(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class ConsentForm(models.Model):
    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_submitted = models.CharField(max_length=100, choices=issubmitted_choice)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        ordering = ('-created_at',)


class PersonnelOptions(models.Model):
    issue_toll_card = models.BooleanField(default=False)
    training = models.BooleanField(default=False)
    share_personal_email = models.BooleanField(default=False)
    post_photo_video_audio = models.BooleanField(default=False)
    voluntary_activity = models.BooleanField(default=False)
    corporate_assets = models.BooleanField(default=False)
    discount_card = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    personnel_options = models.OneToOneField(ConsentForm, on_delete=models.CASCADE, primary_key=True, related_name='personnel_options')

    def __str__(self):
        return ''