from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Model
from django.views import View

from base.settings import AUDIT_ENABLED, SOCIAL_MEDIA, SYSTEM_NAME
from core.views.utils import get_apps


def get_default_context_data(context: dict, view: View):
    """Cria o contexto padrão para as views
    contendo user_ip, system_name, social_media,
    apps, model_name, urls e permissões"""

    app = view.model._meta.app_label
    model = view.model._meta.model_name

    context["user_ip"] = view.request.META.get(
        "HTTP_X_FORWARDED_FOR"
    ) or view.request.META.get("REMOTE_ADDR")

    context["system_name"] = SYSTEM_NAME
    context["social_media"] = SOCIAL_MEDIA
    context["apps"] = get_apps()
    context["model_name"] = (
        view.model._meta.verbose_name
        or view.model._meta.verbose_name_plural
        or view.model._meta.object_name
        or view.model._meta.model_name
    ).title()

    context = get_default_urls(context, app, model)
    context = check_permissions(context, view.request, view.model())

    context["audit"] = getattr(view.model._meta, "auditar", AUDIT_ENABLED)

    return context


def get_default_urls(context: dict, app: str, model: str):
    """Adiciona as urls padrão ao context das views"""
    context["url_create"] = f"{app}:{model}-create"
    context["url_update"] = f"{app}:{model}-update"
    context["url_detail"] = f"{app}:{model}-detail"
    context["url_list"] = f"{app}:{model}-list"
    context["url_delete"] = f"{app}:{model}-delete"
    return context


def check_permissions(context: dict, request: WSGIRequest, model: Model):
    """Adiciona as permissões padrão ao context das views"""
    context["has_add_permission"] = model.has_add_permission(request)
    context["has_change_permission"] = model.has_change_permission(request)
    context["has_delete_permission"] = model.has_delete_permission(request)
    context["has_view_permission"] = model.has_view_permission(request)
    return context
