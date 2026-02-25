import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from sales.models import Sale

class Command(BaseCommand):
    help = 'Importe les données de ventes depuis le fichier ecommerce_sales_data.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Le chemin vers le fichier CSV')

    def handle(self, *args, **options):
        file_path = options['csv_file']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                sales_to_create = []

                for row in reader:
                    # Conversion de la date (Format attendu: YYYY-MM-DD)
                    order_date = datetime.strptime(row['Order Date'], '%Y-%m-%d').date()

                    # Préparation de l'objet Sale
                    sale = Sale(
                        order_date=order_date,
                        product_name=row['Product Name'],
                        category=row['Category'],
                        region=row['Region'],
                        quantity=int(row['Quantity']),
                        sales_amount=float(row['Sales']),
                        profit=float(row['Profit'])
                    )
                    sales_to_create.append(sale)

                # Utilisation de bulk_create pour une insertion massive rapide
                Sale.objects.bulk_create(sales_to_create)
                
                self.stdout.write(self.style.SUCCESS(f'Succès : {len(sales_to_create)} ventes importées !'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Fichier non trouvé à l\'emplacement : {file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erreur lors de l\'importation : {str(e)}'))