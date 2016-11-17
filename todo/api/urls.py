from api.views import BucketlistViewSets, LoginView
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^bucketlists', BucketlistViewSets)
#router.register(r'bucketlists/(?P<id>[0-9]+)$', SingleBucketlistViewSets)
urlpatterns = router.urls + [
    url(r'^login$', LoginView.as_view(), name='api_login')
]
