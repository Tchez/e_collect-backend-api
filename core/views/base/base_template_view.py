from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView

from base.settings import SOCIAL_MEDIA, SYSTEM_NAME
from core.views.utils import get_apps


class BaseTemplateView(TemplateView):
    """
    Classe base que deve ser herdada caso o desenvolvedor queira reaproveitar
    as funcionalidades já desenvolvidas TemplateView

    Na classe que herdar dessa deve ser atribuido o valor template_name com o caminho até o template HTML a ser renderizado

    Raises:
        ValidationError -- Caso não seja atribuido o valor da variavel template_name ocorrerá uma excessão
    """

    def __init__(self):
        if self.template_name is None:
            raise ValidationError(
                message='Deve ser definido o caminho do template na variavel "template_name" em sua Views!'
            )
        super(BaseTemplateView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        context["user_ip"] = self.request.META.get(
            "HTTP_X_FORWARDED_FOR"
        ) or self.request.META.get("REMOTE_ADDR")
        context["system_name"] = SYSTEM_NAME
        context["apps"] = get_apps()
        context["social_media"] = SOCIAL_MEDIA
        return context


class BaseIndexTemplate(LoginRequiredMixin, PermissionRequiredMixin, BaseTemplateView):
    """[summary]

    Arguments:
        BaseTemplateView {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    template_name = "core/index.html"
    context_object_name = "core"

    def has_permission(self):
        """
        Verifica se tem alguma das permissões retornadas pelo
        get_permission_required, caso tenha pelo menos uma ele
        retorna True
        """
        return (
            self.request.user is not None
            and self.request.user.is_authenticated
            and self.request.user.is_active
        )
