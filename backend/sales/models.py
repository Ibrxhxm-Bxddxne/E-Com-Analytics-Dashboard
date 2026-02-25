from django.db import models

class Sale(models.Model):
    # Les catégories et régions peuvent être gérées avec des "choices" pour plus de rigueur
    # Mais pour un dashboard analytique, on les laisse souvent en CharField 
    # pour accepter les nouvelles données du CSV facilement.

    order_date = models.DateField(verbose_name="Date de commande")
    product_name = models.CharField(max_length=255, verbose_name="Nom du produit")
    category = models.CharField(max_length=100, verbose_name="Catégorie")
    region = models.CharField(max_length=100, verbose_name="Région")
    quantity = models.IntegerField(verbose_name="Quantité")
    sales_amount = models.FloatField(verbose_name="Montant des ventes")
    profit = models.FloatField(verbose_name="Profit")

    # Date de création dans la base (utile pour le suivi interne)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-order_date']
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"

    def __str__(self):
        return f"{self.product_name} - {self.order_date} ({self.region})"