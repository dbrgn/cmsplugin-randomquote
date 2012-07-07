from django.db import models
from django.utils.translation import ugettext_lazy as _


class Quote(models.Model):
    quote_text = models.TextField(_(u'Quote Text'))
    author = models.CharField(_(u'Author'), max_length=255)

    def __unicode__(self):
        return '[%s] %s...' % (self.author, self.quote_text[:20])
