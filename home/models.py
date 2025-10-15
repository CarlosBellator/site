from django.db import models

# Create your models here.
class grafico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    descricao = models.TextField()
    x_axis_label = models.CharField(max_length=100)
    y_axis_label = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='graficos/', default='graficos/default.jpg', blank=True)
    obj3d = models.FileField(upload_to='objetos3d/', default='objetos3d/default.obj', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Gráfico {self.name} de {self.user.username}"


class valores_grafico(models.Model):
    grafico = models.ForeignKey(grafico, on_delete=models.CASCADE)
    x_data = models.FloatField()
    y_data = models.FloatField()