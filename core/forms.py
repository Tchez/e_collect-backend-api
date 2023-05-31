from django import forms
from django.forms.fields import BooleanField, DateField, DateTimeField, JSONField
from django.utils.translation import gettext_lazy as _

from .models import Audit, Base


class BaseForm(forms.ModelForm):
    """Form para ser usado no classe based views"""

    # Sobrescrevendo o Init para aplicar as regras CSS
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(BaseForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            # Coleta as classes passadas no Form
            class_attrs = self.fields[field].widget.attrs.get("class", "")

            # Aplica o padrão
            class_attrs += " form-control"

            # Verificando se o campo está configurado como obrigatório
            if self.fields[field].required:
                class_attrs += " obrigatorio"

            # Verificando se o campo é Booleano
            if isinstance(self.fields[field], BooleanField):
                class_attrs += " checked-left"

            # Verificando se o campo é do tipo DateTime
            if isinstance(self.fields[field], DateTimeField):
                class_attrs += " datetimefield"
                self.fields[field].widget.attrs.update({"placeholder": "dd/mm/aaaa hh:mm"})

            # Verificando se o campo é do tipo Date
            if isinstance(self.fields[field], DateField):
                class_attrs += " datefield"
                self.fields[field].widget.attrs.update({"placeholder": "dd/mm/aaaa"})

            # # Verificando se o campo é do tipo FileField
            # if isinstance(self.fields[field], FileField):
            #     class_attrs += " custom-file-input"

            # # Verificando se o campo é do tipo ImageField
            # if isinstance(self.fields[field], ImageField):
            #     class_attrs += " custom-file-input"

            # # Verificando se o campo é do tipo BooleanField
            if isinstance(self.fields[field], BooleanField):
                class_attrs += " form-check-input"

            # Atualizando os atributos do campo para adicionar as classes
            # conforme as regras anteriores
            self.fields[field].widget.attrs.update({"class": class_attrs.lstrip()})

    class Meta:
        model = Base
        exclude = ["enabled", "deleted"]


"""
=========================================================================
=========================================================================
=========================================================================
=========================================================================
=========================================================================
=========================================================================
                    Área dos models de Auditoria
=========================================================================
=========================================================================
=========================================================================
=========================================================================
=========================================================================
=========================================================================
"""


class AuditForm(forms.ModelForm):
    previous_data_change = JSONField(help_text=_("before the time of the change"))
    current_data = JSONField(help_text=_("data at the time of the change"))
    user_change = JSONField(label=_("user"), help_text=_("user who changed the data"))
    user_permissions_change = JSONField(label=_("user permissions"), help_text=_("permissions at the time of change"))
    user_groups_change = JSONField(label=_("user groups"), help_text=_("groups at the time of change"))

    class Meta:
        fields = "__all__"
        model = Audit
