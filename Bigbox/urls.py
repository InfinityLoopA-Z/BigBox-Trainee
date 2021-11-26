from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from apps.polls.schema import schema


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('polls/', include('apps.polls.urls')),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # noqa

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
