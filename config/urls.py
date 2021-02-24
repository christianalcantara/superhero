from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView
from graphql_jwt.decorators import jwt_cookie
from graphql_playground.views import GraphQLPlaygroundView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "graphql", csrf_exempt(jwt_cookie(FileUploadGraphQLView.as_view(graphiql=True)))
    ),
    path("", GraphQLPlaygroundView.as_view(endpoint=settings.GRAPHQL_ENDPOINT)),
]

if settings.DEBUG:
    urlpatterns.append(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)[0]
    )
    urlpatterns.append(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)[0])
