from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/apidrf', ProjectViewSet, 'apidrf')

urlpatterns = router.urls