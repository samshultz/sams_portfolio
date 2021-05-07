import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Skill(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


    def __str__(self):
        return self.name

class StackCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "stack category"
        verbose_name_plural = "stack categories"

    def __str__(self):
        return self.name


class TechStack(models.Model):
    category = models.ForeignKey(StackCategory, related_name="stacks", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField(validators=[
        MaxValueValidator(datetime.date.today, "Start date cannot exceed current date")])
    end_date = models.DateField(null=True, blank=True, validators=[
        MaxValueValidator(datetime.date.today, "End date cannot exceed current date")])
    description = models.TextField()
    currently_working_here = models.BooleanField(default=False)

    class Meta:
        ordering = "start_date",

    def __str__(self):
        return f"{self.position} at {self.company}"

    def save(self, *args, **kwargs):
        # user can only set either end date or if he is currently working her
        # but not both
        if self.end_date and self.currently_working_here:
            raise ValidationError(_("You can either set the End date or Currently working here but not both."))
        # user must set at least one of end date or currently working here
        if not self.end_date and not self.currently_working_here:
            raise ValidationError(_("You must set the date you stopped working here"))
        
        # ensure user only enters start dates before today or today
        if (self.start_date > datetime.date.today()) or (self.end_date > datetime.date.today()):
            raise ValidationError(_("Start or end date cannot exceed current date"))

        # ensure start date is not later than end date
        if self.start_date > self.end_date:
            raise ValidationError(_("Start date cannot be later than End date"))
        return super(WorkExperience, self).save(*args, **kwargs)

