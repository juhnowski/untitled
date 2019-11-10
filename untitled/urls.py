from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'requests', views.RequestViewSet)
router.register(r'words', views.WordViewSet)
router.register(r'stopwords', views.StopWordViewSet)
router.register(r'totalindex', views.TotalIndexViewSet)
router.register(r'wordinrequest', views.WordInRequestViewSet)
router.register(r'wordpositionsinrequest', views.WordPositionsInRequestViewSet)
router.register(r'requestresponse', views.RequestResponseViewSet)


schema_view = get_swagger_view(title='Test App API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', schema_view),
]
