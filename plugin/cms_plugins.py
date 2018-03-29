from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import *

@plugin_pool.register_plugin
class NewsPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "news.html"
    cache = False
    
    def render(self, context, instance, placeholder):
        news = News.objects.all()
        context['news'] = news
        context = super(NewsPlugin, self).render(context, instance, placeholder)
        context.update({
            'news': news,
        })
        return context



