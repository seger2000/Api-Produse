from magazinAPI.viewsets import ProduseViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produse', ProduseViewset)