from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_agtec_core.models import DadosGerais, Gestor, ImagemLogin, LogoSistema


class GestorSerializer(ModelSerializer):
    """Class do serializer do model Gestor para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Gestor
        exclude = ["deleted", "enabled"]


class GestorGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Gestor para o GET"""

    class Meta:
        model = Gestor
        exclude = ["deleted", "enabled"]


class ImagemLoginSerializer(ModelSerializer):
    """Class do serializer do model ImagemLogin para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = ImagemLogin
        exclude = ["deleted", "enabled"]


class ImagemLoginGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model ImagemLogin para o GET"""

    class Meta:
        model = ImagemLogin
        exclude = ["deleted", "enabled"]


class LogoSistemaSerializer(ModelSerializer):
    """Class do serializer do model LogoSistema para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = LogoSistema
        exclude = ["deleted", "enabled"]


class LogoSistemaGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model LogoSistema para o GET"""

    class Meta:
        model = LogoSistema
        exclude = ["deleted", "enabled"]


class DadosGeraisSerializer(ModelSerializer):
    """Class do serializer do model DadosGerais para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = DadosGerais
        exclude = ["deleted", "enabled"]


class DadosGeraisGETSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model DadosGerais para o GET"""

    class Meta:
        model = DadosGerais
        exclude = ["deleted", "enabled"]
