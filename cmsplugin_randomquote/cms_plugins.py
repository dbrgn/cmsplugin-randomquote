from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Quote


class QuotePlugin(CMSPluginBase):
    """This plugin randomly renders a quote from the database."""
    name = _('Quote')
    render_template = 'cmsplugin_randomquote/quote.html'

    def render(self, context, instance, placeholder):
        try:
            t_obj = Quote.objects.order_by('?')[0]
            context['quote'] = t_obj.quote_text
            context['author'] = t_obj.author
            context['author_url'] = t_obj.author_url
        except IndexError:
            pass

        return context

plugin_pool.register_plugin(QuotePlugin)
