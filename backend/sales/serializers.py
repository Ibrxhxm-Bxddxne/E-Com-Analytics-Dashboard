from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    # On définit des champs calculés ou formatés si besoin
    # Par exemple, formater la date pour un affichage plus propre
    display_date = serializers.DateField(source='order_date', format="%d/%m/%Y", read_only=True)

    class Meta:
        model = Sale
        # On inclut tous les champs du modèle + notre champ personnalisé
        fields = [
            'id', 
            'order_date', 
            'display_date', 
            'product_name', 
            'category', 
            'region', 
            'quantity', 
            'sales_amount', 
            'profit'
        ]

    # Optionnel : Validation personnalisée
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("La quantité doit être supérieure à zéro.")
        return value

    def validate_sales_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Le montant des ventes ne peut pas être négatif.")
        return value