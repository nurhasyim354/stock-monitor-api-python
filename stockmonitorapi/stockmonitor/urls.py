from django.urls import re_path
from stockmonitor import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Stock Monitor API",
        default_version='v1',
        description="This apis are built using Python, Django, and Mongodb",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nurhasyim.byu@gmail.com"),
        license=openapi.License(name="None"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
    re_path(r'^api/stocks$', views.stocks),
    re_path(r'^api/stock/(?P<pk>[0-9]+)$', views.stock_details)
]
