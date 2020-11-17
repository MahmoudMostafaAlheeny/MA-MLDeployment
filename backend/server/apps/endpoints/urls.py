from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgoViewSet
from apps.endpoints.views import MLAlgoStatusSet
from apps.endpoints.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"endpoints",EndpointViewSet,basename="endpoints")
router.register(r"mlalgo",MLAlgoViewSet,basename="mlalgo")
router.register(r"mlagostatuses",MLAlgoStatusSet,basename="mlalgostatus")
router.register(r"mlrequests",MLRequestViewSet,basename="mlrequests")

urlpatterns = [url(r"^api/v1/", include(router.urls)),]

