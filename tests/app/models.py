from django.db import models
from django.utils.translation import gettext_lazy as _


class Page(models.Model):
    header = models.CharField(_('header'), max_length=255)
    order = models.PositiveIntegerField(_('order'), default=0, editable=False)

    class Meta:
        ordering = ['order']
        verbose_name = _('page')
        verbose_name_plural = _('pages')

    def __str__(self):
        return self.header
