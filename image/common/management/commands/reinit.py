from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('resetdb')
        management.call_command('makemigrations')
        management.call_command('migrate')
        management.call_command('initdata')
        management.call_command('create_test_data')
        management.call_command('import_usdt_address')
