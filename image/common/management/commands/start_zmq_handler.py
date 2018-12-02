from django.core.management.base import BaseCommand

from utils_blockchain.zmq_sub import ZMQHandler


class Command(BaseCommand):
    def handle(self, *args, **options):
        daemon = ZMQHandler()
        daemon.start()
