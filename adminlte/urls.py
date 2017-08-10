from django.conf.urls import include, url
from django.contrib import admin

from proceeds.views import view_proceeds, get_selected

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_selected/', get_selected),
    url(r'^', view_proceeds),
]
