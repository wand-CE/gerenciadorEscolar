from django.views.generic import TemplateView

from core.models import Curso, Disciplina


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()

        return context




