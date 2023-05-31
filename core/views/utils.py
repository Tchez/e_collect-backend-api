import logging
from uuid import UUID

from base.settings import IGNORED_APPS as IGNORED_APPS_BASE
from core.views.constants import IGNORED_APPS, IGNORED_MODELS
from django.contrib.contenttypes.models import ContentType
from django.utils.text import camel_case_to_spaces

# Configurando o logger
logger = logging.getLogger(__name__)


def has_fk_attr(classe=None, attr=None):
    try:
        classe.objects.values(attr)

    except Exception:
        return False

    return True


def get_breadcrumbs(url_str):
    """
    Método para criar o Breadcrumbs a ser utilizado nos templastes
    Arguments:
        url_str {String} -- [Nome da app e do Models]
    Returns:
        [Lista] -- [Lista com o breadcrumb]
    """

    breadcrumbs = [
        {
            "slug": "Inicio",
            "url": "/",
        }
    ]
    url = "/"

    array_url = url_str.strip("/").split("/")
    for cont, slug in enumerate(array_url, start=1):
        breadcrumb = {}

        if slug != "":
            if isinstance(slug, UUID):
                breadcrumb["slug"] = ContentType.objects.get(
                    app_label=array_url[1], model=array_url[2]
                ).model_class().objects.get(pk=slug)

            else:
                breadcrumb["slug"] = camel_case_to_spaces(slug).title()

            if cont < len(array_url):
                url = f"{url}{slug.lower()}/"
                breadcrumb["url"] = url

            breadcrumbs.append(breadcrumb)

    return breadcrumbs


def get_apps():
    """Método para recuperar todas as apps

    Returns:
        List -- Lista com as apps que o usuário tem acesso
    """

    from django.apps import apps

    _apps = []
    for app in apps.get_app_configs():

        try:
            if app.name in IGNORED_APPS or app.name in IGNORED_APPS_BASE:
                continue

            _models = []
            app_models = sorted(app.get_models(), key=lambda x: x._meta.verbose_name)
            for model in app_models:
                if model._meta.model_name in IGNORED_MODELS:
                    continue

                __model_icon = (
                    model._meta.icon_model
                    if hasattr(model._meta, "icon_model")
                    else "fas fa-angle-right"
                )

                _models.append(
                    {
                        "name_model": model._meta.verbose_name,
                        "url_list_model": "/{app}/{model}/".format(
                            app=model._meta.app_label, model=model._meta.model_name
                        ),
                        "path_url": "{app}:{model}-list".format(
                            app=model._meta.app_label.lower(),
                            model=model._meta.model_name.lower(),
                        ),
                        "real_name_model": model._meta.model_name,
                        "icon_model": __model_icon,
                    }
                )

            if _models:
                icon = app.icon if hasattr(app, "icon") else "fas fa-align-justify"

            _apps.append(
                {
                    "name_app": f"{app.verbose_name}",
                    "icon_app": icon,
                    "models_app": _models,
                    "index_url_app": f"{model._meta.app_label}:{model._meta.app_label}-index",
                    "real_name_app": app.name,
                    "real_name_model": model._meta.model_name,
                }
            )

        except Exception as error:
            print(error)
            continue

    return sorted(_apps, key=lambda x: x["name_app"])
