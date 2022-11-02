from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ConsentForm(models.Model):
    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_submitted = models.BooleanField(default=False)
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
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    personnel_options = models.OneToOneField(ConsentForm, on_delete=models.CASCADE, primary_key=True, related_name='personnel_options')

    def __str__(self):
        return ''