from rest_framework import routers

from .api_views import (
    DadosGeraisCustomViewAPI,
    DadosGeraisViewAPI,
    GestorCustomViewAPI,
    GestorViewAPI,
    ImagemLoginCustomViewAPI,
    ImagemLoginViewAPI,
    LogoSistemaCustomViewAPI,
    LogoSistemaViewAPI,
)

router = routers.DefaultRouter()

# URL para a API Gestor
router.register(r"gestor", GestorViewAPI, "gestor-api")
router.register(r"gestor/custom", GestorCustomViewAPI, "gestor-get-api")


# URL para a API ImagemLogin
router.register(r"imagemlogin", ImagemLoginViewAPI, "imagemlogin-api")
router.register(r"imagemlogin/custom", ImagemLoginCustomViewAPI, "imagemlogin-get-api")


# URL para a API LogoSistema
router.register(r"logosistema", LogoSistemaViewAPI, "logosistema-api")
router.register(r"logosistema/custom", LogoSistemaCustomViewAPI, "logosistema-get-api")


# URL para a API DadosGerais
router.register(r"dadosgerais", DadosGeraisViewAPI, "dadosgerais-api")
router.register(r"dadosgerais/custom", DadosGeraisCustomViewAPI, "dadosgerais-get-api")

urlpatterns = router.urls
