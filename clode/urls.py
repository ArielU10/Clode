from django.urls import path, include
from rest_framework import routers
from clode import views
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'users', views.UsersView, basename='users')
router.register(r'user_preferences', views.UsersPreferencesView, basename='user_preferences')
router.register(r'garments', views.GarmentsView, basename='garments')
router.register(r'garment_tags', views.GarmentTagsView, basename='garment_tags')
router.register(r'exchange', views.ExchangeView, basename='exchange')
# router.register(r'scores', views.ScoresView, basename='scores')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title="clode API"))
]