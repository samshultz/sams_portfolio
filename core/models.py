from django.db import models


class Skills(models.Model):
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

    def __str__(self):
        return f"{self.position} at {self.company}"

    
    class Meta:
        ordering = "start_date",
