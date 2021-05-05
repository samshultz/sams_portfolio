from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AboutMe(models.Model):
    AVAILABLE = 'available'
    NOT_AVAILABLE = 'not available'

    FREELANCE_CHOICES = (
        (AVAILABLE, 'Available'),
        (NOT_AVAILABLE, 'Not Available')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="about_me")

    description = models.TextField()
    phone = models.CharField(_("Phone Number"), max_length=50)
    freelance = models.CharField(choices=FREELANCE_CHOICES, default=AVAILABLE, max_length=13)

    
    class Meta:
        """Meta definition for AboutMe."""

        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk and AboutMe.objects.exists():
            raise ValidationError(_("There can only be one about me."))
        return super(AboutMe, self).save(*args, **kwargs)


    @property
    def email(self):
        return self.user.email
    
    @property
    def fullname(self):
        return self.user.get_full_name()

