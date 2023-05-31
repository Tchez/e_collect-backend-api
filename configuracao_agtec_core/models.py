from django.db import models

from core.models import Base


class Gestor(Base):
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")
    funcao = models.CharField("Função", max_length=100)
    telefone = models.CharField("Telefone", max_length=11)
    assinatura = models.ImageField("Assinatura", upload_to="assinaturas", blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.funcao}"

    class Meta:
        verbose_name = "Gestor"
        verbose_name_plural = "Gestores"
        fields_display = ["nome", "email", "funcao", "telefone", "assinatura"]
        icon_model = "fa fa-user"
        db_table = "configuracao_gestor"


class ImagemLogin(Base):
    imagem = models.ImageField("Imagem de login", upload_to="imagens_login")
    ativo = models.BooleanField("Ativo", default=True)
    login_usuario = models.BooleanField("Login de Usuário?", default=False)

    def __str__(self):
        return str(self.imagem)

    class Meta:
        verbose_name = "Imagem de Login"
        verbose_name_plural = "Imagens de Login"
        fields_display = ["imagem", "ativo"]
        icon_model = "fa fa-image"
        db_table = "configuracao_imagem_login"


class LogoSistema(Base):
    imagem = models.ImageField("Logo do Sistema", upload_to="logos")
    ativo = models.BooleanField("Ativo", default=True)

    def __str__(self):
        return str(self.imagem)

    class Meta:
        verbose_name = "Logo do Sistema"
        verbose_name_plural = "Logos do Sistema"
        fields_display = ["imagem", "ativo"]
        icon_model = "fa fa-image"
        db_table = "configuracao_logo_sistema"


class DadosGerais(Base):
    telefone = models.CharField("Telefone", max_length=11)
    endereco = models.CharField("Endereço", max_length=100)
    horario_atendimento = models.CharField("Horário de atendimento", max_length=100)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Dados Gerais"
        verbose_name_plural = "Dados Gerais"
        fields_display = ["telefone", "endereco", "horario_atendimento"]
        icon_model = "fa fa-info"
        db_table = "configuracao_dados_gerais"
