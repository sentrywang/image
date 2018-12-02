import os.path

from django.conf import settings
from django.core.management.base import BaseCommand
from utils_blockchain.models import UsdtAddress


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('importing USDT addresses...')
        if settings.DEV_MODE:
            address_file = 'addresses-testnet.txt'
        else:
            address_file = 'addresses-mainnet.txt'

        address_file = os.path.join(os.path.join(settings.BASE_DIR, 'assets'), address_file)

        with open(address_file, 'r') as f:
            for line in f.readlines():
                address = line.split()[0]
                UsdtAddress.objects.get_or_create(address=address)
