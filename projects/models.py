from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Project(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField('projects.Category', related_name="projects")

    name = models.CharField(_('Name'), max_length=250)
    description = models.TextField()
    image = models.ImageField(_('Project Image'), upload_to='projects/img')
    url = models.URLField(_("Project's URL"), max_length=200)

    class Meta:
        ordering = "-id",

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
