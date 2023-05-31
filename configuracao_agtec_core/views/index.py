from core.views.base import BaseTemplateView


# Views Inicial Configuracao_Agtec_Core
class Configuracao_Agtec_CoreIndexTemplateView(BaseTemplateView):
    # Views para renderizar a tela inicial Configuracao_Agtec_Core
    template_name = "configuracao_agtec_core/index.html"
    context_object_name = "configuracao_agtec_core"

    def get_context_data(self, **kwargs):
        context = super(Configuracao_Agtec_CoreIndexTemplateView, self).get_context_data(**kwargs)
        return context
