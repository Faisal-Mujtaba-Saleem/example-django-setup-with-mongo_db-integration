from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

# Define the DRF router and register the StudentViewSet
router = DefaultRouter()
router.register(prefix=r'students', viewset=StudentViewSet, basename='student')

# The URLs generated by the router
urlpatterns = router.urls
