from graphene_django.views import GraphQLView
from home.schema import schema
from django.urls import path

urlpatterns = [
    path('quiz/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
