from rest_framework import routers
from .api import TeaserViewSet


router = routers.DefaultRouter()
router.register('api/teaser', TeaserViewSet, 'teaser')

urlpatterns = router.urls
