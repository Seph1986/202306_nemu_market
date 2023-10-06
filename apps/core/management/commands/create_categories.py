""" Script create categories. """
from django.core.management.base import BaseCommand
from apps.motor_app.models import MotorCategory
from apps.entertainments.models import EntertainmentCategory
from apps.furnitures.models import FurnitureCategory
from apps.electronics.models import ElectronicCategory

class Command(BaseCommand):
    """ Comando para crear categorías. """
    help = 'Create initial categories'

    def handle(self, *args, **options):
        categories_data = [
            (MotorCategory, ['Automóviles', 'Motocicletas', 'Náutica', 'Camiones', 'Otros de Motorizados']),
            (EntertainmentCategory, ['Música', 'Libros', 'Deportes', 'Aire libre', 'Otros de Entretenimiento']),
            (FurnitureCategory, ['Cocina', 'Baño', 'Sala de Estar', 'Patio', 'Comedor', 'Otros de mobiliarios', ]),
            (ElectronicCategory, ['Computadoras', 'Celulares', 'Tablets', 'TV - Audio - Video', 'Cámaras - Accesorios', 'Videojuegos - Consolas', 'Otros de Electrónica']),
        ]

        for category_model, category_names in categories_data:
            for category_name in category_names:
                category_model.objects.get_or_create(name=category_name)

        self.stdout.write(self.style.SUCCESS('Successfully created categories'))