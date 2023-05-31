from django.urls import path

from .views import (
    Configuracao_Agtec_CoreIndexTemplateView,
    DadosGeraisCreateView,
    DadosGeraisDeleteView,
    DadosGeraisDetailView,
    DadosGeraisListView,
    DadosGeraisRestoreView,
    DadosGeraisUpdateView,
    GestorCreateView,
    GestorDeleteView,
    GestorDetailView,
    GestorListView,
    GestorRestoreView,
    GestorUpdateView,
    ImagemLoginCreateView,
    ImagemLoginDeleteView,
    ImagemLoginDetailView,
    ImagemLoginListView,
    ImagemLoginRestoreView,
    ImagemLoginUpdateView,
    LogoSistemaCreateView,
    LogoSistemaDeleteView,
    LogoSistemaDetailView,
    LogoSistemaListView,
    LogoSistemaRestoreView,
    LogoSistemaUpdateView,
)

app_name = "configuracao_agtec_core"

# URLs do Models Gestor
urlpatterns = [
    path(
        "configuracao_agtec_core/",
        Configuracao_Agtec_CoreIndexTemplateView.as_view(),
        name="configuracao_agtec_core-index",
    ),
    path("configuracao_agtec_core/gestor/", GestorListView.as_view(), name="gestor-list"),
    path("configuracao_agtec_core/gestor/create/", GestorCreateView.as_view(), name="gestor-create"),
    path("configuracao_agtec_core/gestor/<uuid:pk>/", GestorDetailView.as_view(), name="gestor-detail"),
    path("configuracao_agtec_core/gestor/update/<uuid:pk>/", GestorUpdateView.as_view(), name="gestor-update"),
    path("configuracao_agtec_core/gestor/delete/<uuid:pk>/", GestorDeleteView.as_view(), name="gestor-delete"),
    path("configuracao_agtec_core/gestor/restore/<uuid:pk>/", GestorRestoreView.as_view(), name="gestor-restore"),
]


# URLs do Models ImagemLogin
urlpatterns += [
    path(
        "configuracao_agtec_core/",
        Configuracao_Agtec_CoreIndexTemplateView.as_view(),
        name="configuracao_agtec_core-index",
    ),
    path("configuracao_agtec_core/imagemlogin/", ImagemLoginListView.as_view(), name="imagemlogin-list"),
    path("configuracao_agtec_core/imagemlogin/create/", ImagemLoginCreateView.as_view(), name="imagemlogin-create"),
    path("configuracao_agtec_core/imagemlogin/<uuid:pk>/", ImagemLoginDetailView.as_view(), name="imagemlogin-detail"),
    path(
        "configuracao_agtec_core/imagemlogin/update/<uuid:pk>/",
        ImagemLoginUpdateView.as_view(),
        name="imagemlogin-update",
    ),
    path(
        "configuracao_agtec_core/imagemlogin/delete/<uuid:pk>/",
        ImagemLoginDeleteView.as_view(),
        name="imagemlogin-delete",
    ),
    path(
        "configuracao_agtec_core/imagemlogin/restore/<uuid:pk>/",
        ImagemLoginRestoreView.as_view(),
        name="imagemlogin-restore",
    ),
]


# URLs do Models LogoSistema
urlpatterns += [
    path(
        "configuracao_agtec_core/",
        Configuracao_Agtec_CoreIndexTemplateView.as_view(),
        name="configuracao_agtec_core-index",
    ),
    path("configuracao_agtec_core/logosistema/", LogoSistemaListView.as_view(), name="logosistema-list"),
    path("configuracao_agtec_core/logosistema/create/", LogoSistemaCreateView.as_view(), name="logosistema-create"),
    path("configuracao_agtec_core/logosistema/<uuid:pk>/", LogoSistemaDetailView.as_view(), name="logosistema-detail"),
    path(
        "configuracao_agtec_core/logosistema/update/<uuid:pk>/",
        LogoSistemaUpdateView.as_view(),
        name="logosistema-update",
    ),
    path(
        "configuracao_agtec_core/logosistema/delete/<uuid:pk>/",
        LogoSistemaDeleteView.as_view(),
        name="logosistema-delete",
    ),
    path(
        "configuracao_agtec_core/logosistema/restore/<uuid:pk>/",
        LogoSistemaRestoreView.as_view(),
        name="logosistema-restore",
    ),
]


# URLs do Models DadosGerais
urlpatterns += [
    path(
        "configuracao_agtec_core/",
        Configuracao_Agtec_CoreIndexTemplateView.as_view(),
        name="configuracao_agtec_core-index",
    ),
    path("configuracao_agtec_core/dadosgerais/", DadosGeraisListView.as_view(), name="dadosgerais-list"),
    path("configuracao_agtec_core/dadosgerais/create/", DadosGeraisCreateView.as_view(), name="dadosgerais-create"),
    path("configuracao_agtec_core/dadosgerais/<uuid:pk>/", DadosGeraisDetailView.as_view(), name="dadosgerais-detail"),
    path(
        "configuracao_agtec_core/dadosgerais/update/<uuid:pk>/",
        DadosGeraisUpdateView.as_view(),
        name="dadosgerais-update",
    ),
    path(
        "configuracao_agtec_core/dadosgerais/delete/<uuid:pk>/",
        DadosGeraisDeleteView.as_view(),
        name="dadosgerais-delete",
    ),
    path(
        "configuracao_agtec_core/dadosgerais/restore/<uuid:pk>/",
        DadosGeraisRestoreView.as_view(),
        name="dadosgerais-restore",
    ),
]
