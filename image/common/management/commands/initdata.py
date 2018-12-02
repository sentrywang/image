from django.core.management.base import BaseCommand

from agent.models import Agent
from myuser.models import UserProfile
from staff.models import Staff


class Command(BaseCommand):

    def create_super_admin(self):
        print('creating super admin...')
        if not Staff.objects.filter(username='admin01').exists():
            Staff.objects.create_staff(
                username='admin01', email='btcmanbbs@protonmail.com', password='V3ryG0Od#', is_super_admin=True,
            )

    def create_agent(self):
        print('creating agent...')
        if not Agent.objects.filter(username='agent01').exists():
            Agent.objects.create_agent(username='agent01', email='', password='V3ryG0Od#')

    def create_sys_user(self):
        print('creating system user...')
        if not UserProfile.objects.filter(username='system').exists():
            sys = UserProfile.objects.create_user(
                username='system', email='', password=''
            )
            sys.balance = 100000
            sys.save()

    def handle(self, *args, **options):
        self.create_super_admin()
        self.create_sys_user()
