from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum, Avg
from .models import Sale
from .serializers import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):
    """
    Cette vue fournit automatiquement les actions 'list', 'create', 'retrieve',
    'update' et 'destroy'.
    """
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
    # Gestion des permissions : Authentification requise pour modifier les données
    # Vous pouvez changer par permissions.AllowAny pour les tests
    permission_classes = [permissions.IsAuthenticated]

    # --- ENDPOINT SUPPLÉMENTAIRE POUR LE DASHBOARD ---
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """
        Endpoint personnalisé pour récupérer les chiffres clés du dashboard.
        URL: /api/sales/stats/
        """
        total_sales = Sale.objects.aggregate(Sum('sales_amount'))['sales_amount__sum'] or 0
        total_profit = Sale.objects.aggregate(Sum('profit'))['profit__sum'] or 0
        avg_profit = Sale.objects.aggregate(Avg('profit'))['profit__avg'] or 0
        count = Sale.objects.count()

        return Response({
            'total_revenue': round(total_sales, 2),
            'total_profit': round(total_profit, 2),
            'average_profit': round(avg_profit, 2),
            'total_orders': count,
        })

    @action(detail=False, methods=['get'])
    def chart_data(self, request):
        """
        Données groupées pour les graphiques (ex: ventes par catégorie).
        URL: /api/sales/chart_data/
        """
        data = Sale.objects.values('category').annotate(total=Sum('sales_amount')).order_factory('-total')
        return Response(data)