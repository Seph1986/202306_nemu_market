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
            (MotorCategory, ['Otros de Motorizados', 'Motocicletas', 'Náutica', 'Camiones', 'Automóviles']),
            (EntertainmentCategory, ['Otros de Entretenimiento', 'Libros', 'Deportes', 'Aire libre', 'Música']),
            (FurnitureCategory, ['Otros de mobiliarios', 'Baño', 'Sala de Estar', 'Patio', 'Comedor', 'Cocina', ]),
            (ElectronicCategory, ['Otros de Electrónica', 'Celulares', 'Tablets', 'TV - Audio - Video', 'Cámaras - Accesorios', 'Videojuegos - Consolas', 'Computadoras']),
        ]

        for category_model, category_names in categories_data:
            for category_name in category_names:
                category_model.objects.get_or_create(name=category_name)

        self.stdout.write(self.style.SUCCESS('Successfully created categories'))