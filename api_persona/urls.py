from rest_framework.routers import DefaultRouter
from api.views import PersonaViewSet,TipoPersonaViewSet

router = DefaultRouter()

router.register('api/tipopersona', TipoPersonaViewSet)
router.register('api/persona', PersonaViewSet)

#Otras rutas

urlpatterns = []

urlpatterns += router.urls

