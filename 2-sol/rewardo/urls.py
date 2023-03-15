from django.contrib import admin
from django.urls import path, include, re_path
from board import views
from board.urls import urlpatterns as board_urlpatterns
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rewardo.settings import STAGE
from rest_framework import permissions


router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title='Reward Service API',
        default_version='v1',
        description='API for rewarding users with points for completing tasks',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # patterns=[
    #     path('api/', include(router.urls)),
    #     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #     path('docs/', include_docs_urls(title='My API')),
    # ] + board_urlpatterns
)

urlpatterns = [
    # Django JET URLS
    path('jet/', include('jet.urls', 'jet')),

    # Django JET dashboard URLS
    path('jet/dashboard/', include('jet.dashboard.urls',
         'jet-dashboard')),

    path('api-auth/', include('rest_framework.urls')),

    # all-auth accounts URLs
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),

    # board app URLS
    path('', include('board.urls')),
    path('api/v1/', include('board.urls')),
    
    # documentation URLs
    path('docs/', include_docs_urls(title='Reward service API')),
    path('openapi/', schema_view.without_ui(cache_timeout=0)),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='redoc-ui'),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.STAGE =='development':
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]