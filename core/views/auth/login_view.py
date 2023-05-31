from base.settings import SYSTEM_NAME
from configuracao_agtec_core.models import ImagemLogin, LogoSistema
from django.contrib.auth.views import LoginView


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "core/registration/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context["background"] = (
            ImagemLogin.objects.filter(ativo=True, login_usuario=False)
            .order_by("?")
            .first()
        )
        context["logo"] = LogoSistema.objects.filter(ativo=True).order_by("?").first()
        context["system_name"] = SYSTEM_NAME
        return context
