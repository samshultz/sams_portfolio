from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


    def __str__(self):
        return self.name


class TechStack(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    currently_working_here = models.BooleanField(default=False)

    class Meta:
        ordering = "start_date",

    def __str__(self):
        return f"{self.position} at {self.company}"

    def save(self, *args, **kwargs):
        if self.end_date and self.currently_working_here:
            raise ValidationError(_("You can either set the End date or Currently working here but not both."))
        if not self.end_date and not self.currently_working_here:
            raise ValidationError(_("You must set the date you stopped working here"))
        return super(WorkExperience, self).save(*args, **kwargs)

