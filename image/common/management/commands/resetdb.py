from django.conf import settings
from django.core.management.base import BaseCommand

import MySQLdb as Database


class Command(BaseCommand):
    def handle(self, *args, **options):
        database = settings.DATABASES['default']
        name = database['NAME']
        host = database['HOST']
        user = database['USER']
        password = database['PASSWORD']

        connection = Database.connect(host=host, user=user, passwd=password)
        connection.query(f'DROP DATABASE IF EXISTS `{name}`;')
        connection.query(f'CREATE DATABASE `{name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
