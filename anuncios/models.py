from django.db import models
from django.conf import settings

class Carro(models.Model):
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    foto_principal = models.ImageField(upload_to='carros/', blank=True, null=True)  # Foto principal opcional
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class FotoCarro(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='carros/')

    def __str__(self):
        return f"Foto de {self.carro}"
