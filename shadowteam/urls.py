from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
	url(r'^calendar/', include('happenings.urls', namespace='calendar')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name='homepage'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^team/$', TemplateView.as_view(template_name="team.html"), name='team'),
    url(r'^contact/', include('contact_form.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)