from django.db import models
class Produto(models.Model):
    nomeproduto = models.CharField(max_length=100)
    precounidade = models.DecimalField(max_digits=6, decimal_places=2)
    estoquedisponivel = models.IntegerField()
    class Meta:
        abstract = True
    def __str__(self):
        return self.nomeproduto
class Verduras(Produto):
    class Meta:
        verbose_name_plural = "Verduras"
    
class Frutas(Produto):
    class Meta:
        verbose_name_plural = "Produtos"

class Entrega(models.Model):
    nomecliente = models.CharField(max_length=255)
    localentrega = models.TextField()
    prazoentrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')
    def __str__(self):
        return self.nomecliente

class Pagamento(models.Model):
    formapagamento = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.formapagamento


class Item(models.Model):
    entregaitem = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nomeitem = models.CharField(max_length=100)
    estoqueitem = models.IntegerField()
    precounidadeitem = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return  f"{self.nomeitem}"
