from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Quote(models.Model):
    quote_text = models.TextField(_(u'Quote Text'))
    author = models.CharField(_(u'Author'), max_length=255)
    author_url = models.URLField(_(u'Author URL'), null=True, blank=True, default=None, max_length=255)

    def __str__(self):
        return '[%s] %s...' % (self.author, self.quote_text[:20])
