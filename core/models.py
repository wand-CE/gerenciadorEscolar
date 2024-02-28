from django.db import models


class Aluno(models.Model):
    OPCOES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("NI", "Não Informado"),
    )
    nome = models.CharField(max_length=50)
    sobrenome= models.CharField(max_length=150)
    sexo = models.CharField(choices=OPCOES, max_length=13)
    end_rua = models.CharField(max_length=50)
    end_numero = models.IntegerField()
    end_cep = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Historico(models.Model):
    periodo_realizacao = models.CharField(max_length=100)
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'

    def __str__(self):
        return f'Histórico do aluno {self.aluno}'



class Curso(models.Model):
    nome = models.CharField(max_length=100)
    depto = models.ForeignKey('Departamento', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    num_alunos = models.PositiveSmallIntegerField()
    curso = models.ManyToManyField(Curso, related_name='curso_disciplinas')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome



class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nome