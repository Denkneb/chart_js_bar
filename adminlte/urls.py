from django.conf.urls import include, url
from django.contrib import admin

from proceeds.views import view_proceeds

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', view_proceeds),
]
