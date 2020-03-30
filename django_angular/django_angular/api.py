from rest_framework import routers
from myapp import api_views

router = routers.DefaultRouter()
router.register(r'register', api_views.RegisterViewset)