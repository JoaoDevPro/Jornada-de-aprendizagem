from django.urls import path, include
#from .views import RiscoListView, SolucaoListView
from app_backend import views 
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'risco', views.RiscoListView, 'risco')
router.register(r'solucao', views.SolucaoListView, 'solucao')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="risco api")),
]
