from django.contrib import admin
from core.models import Aluno, Historico, Curso, Disciplina, Departamento


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomecompleto', 'sexo')

    def nomecompleto(self, aluno):
        return aluno

    nomecompleto.short_description='nome'


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('periodo_realizacao', 'aluno')


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'num_alunos')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'depto', 'disciplinas_curso')

    def disciplinas_curso(self, curso):
        return ', '.join(d.nome for d in curso.curso_disciplinas.all()[:2])

    disciplinas_curso.short_description = 'Disciplinas'

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cursos')

    def cursos(self, depto):
        return ' ,'.join(c.nome for c in depto.curso_set.all())

