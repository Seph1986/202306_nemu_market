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
            (MotorCategory, ['Automóviles', 'Camiones', 'Motocicletas', 'Náutica', 'Otros de Motorizados']),
            (EntertainmentCategory, ['Aire libre', 'Deportes', 'Libros', 'Música','Otros de Entretenimiento']),
            (FurnitureCategory, ['Baño', 'Cocina', 'Comedor', 'Patio','Sala de Estar','Otros de mobiliarios']),
            (ElectronicCategory, ['Cámaras - Accesorios', 'Celulares', 'Computadoras',  'Tablets', 'TV - Audio - Video',  'Videojuegos - Consolas', 'Otros de Electrónica',]),
        ]

        for category_model, category_names in categories_data:
            for category_name in category_names:
                category_model.objects.get_or_create(name=category_name)

        self.stdout.write(self.style.SUCCESS('Successfully created categories'))