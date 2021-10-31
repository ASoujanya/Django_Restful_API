#routes from viewset to application

from api.viewsets import apiViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product',apiViewset)

#GET,POST,PUT,DELETE