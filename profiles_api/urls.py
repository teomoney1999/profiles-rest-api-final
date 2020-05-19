from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),

	# '' mean no prefix
	# router.urls return a list of urls in router
	path('', include(router.urls))
]