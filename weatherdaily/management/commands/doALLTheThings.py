from django.core.management import BaseCommand
from weatherdaily import get_weather

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "My test command"

    # A command must define handle()
    def handle(self, *args, **options):
        self.stdout.write("weather related email is sending")

