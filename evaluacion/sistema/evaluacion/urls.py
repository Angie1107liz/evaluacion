from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from evaluacion import views

routerTareas=routers.DefaultRouter()
routerTareas.register(r'',views.tareasView,'/tareas')

urlpatterns = [
    path("api/v1/tareas/", include(routerTareas.urls)),
    path("docs/", include_docs_urls(title="EvaluacionApi"))
]
