"""
URL configuration for school_system project.
"""


from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    info = openapi.Info(
        title="Django School Portal API",
        default_version='v1',
        description="Django School Portal API Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@django.site"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes = (AllowAny,)
)

# api_version = 'v1'

urlpatterns = [
    # admin
    re_path(f"^{settings.ADMIN_URL.strip()}/?", admin.site.urls),

    # urlconfs
    path('', include('main.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('user.urls')),

    # rest_framework (mainly auth)
    path('api-auth/', include('rest_framework.urls')),

    # swagger/redoc
    re_path('^api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(), name='schema-json'),
    re_path('^api/swagger/?$', schema_view.with_ui('swagger'), name='schema-swagger'),
    re_path('^api/redoc/?$', schema_view.with_ui('redoc'), name='schema-redoc'),

    # media/static
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
