from django.conf import settings
from django.core.management.base import BaseCommand

from myuser.models import UserProfile
from match_bet.models import Game, Tournament, Match, PanKou, Outcome
from notice.models import Notice


class Command(BaseCommand):
    test_user_count = 3
    test_users = []

    def create_test_user(self):
        for x in range(1, 1 + self.test_user_count):
            username = f'test0{x}'
            email = f'test0{x}@888666.gg'
            if not UserProfile.objects.filter(username=username).exists():
                user = UserProfile.objects.create_user(
                    username=username, email=email, password='V3ryG0Od#', balance=200,
                )
                user.email_verified = True
                user.save()
                self.test_users.append(user)

    def create_test_pankou(self):
        u1, u2, u3 = self.test_users

        game = Game.objects.create(name='PUBG', short_name='pubg')
        tournament = Tournament.objects.create(game=game, name='Golden Cup', short_name='golden_cup')
        match = Match.create_match(
            game, tournament, 'LGD', 'FTD', 'LGD v.s. FTD', Match.TYPE_4, '2018-02-08 15:30', '2018-02-08 15:25',
            '备注', 'https://douyu.com', False, '', '', '', False
        )
        close = '2020-01-01 00:00'

        pk1 = PanKou.objects.create(match=match, title='胜方', type=PanKou.TYPE_WINNER, bet_close_time=close)
        oc1_1 = Outcome.objects.create(pankou=pk1, title='LGD', odds=1.00)
        oc1_2 = Outcome.objects.create(pankou=pk1, title='FTD', odds=1.00)

        pk2 = PanKou.objects.create(match=match, title='积分更高', type=PanKou.TYPE_HANDICAP, bet_close_time=close)
        oc2_1 = Outcome.objects.create(pankou=pk2, title='FTD', odds=1.00)
        oc2_2 = Outcome.objects.create(pankou=pk2, title='LGD', odds=1.00)

        pk3 = PanKou.objects.create(match=match, title='FTD 积分大小盘', type=PanKou.TYPE_OU, bet_close_time=close)
        oc3_1 = Outcome.objects.create(pankou=pk3, title='> 100.5', odds=1.00)
        oc3_2 = Outcome.objects.create(pankou=pk3, title='< 100.5', odds=1.00)

        pk4 = PanKou.objects.create(match=match, title='FTD 能否吃鸡', type=PanKou.TYPE_2, bet_close_time=close)
        oc4_1 = Outcome.objects.create(pankou=pk4, title='能', odds=1.00)
        oc4_2 = Outcome.objects.create(pankou=pk4, title='否', odds=1.00)

        Outcome.place_bet(outcome_id=oc1_1.id, user=u1, amount=10)
        Outcome.place_bet(outcome_id=oc1_2.id, user=u2, amount=20)

    def create_test_notice(self):
        Notice.objects.create(content='test content1', title='test title1',
                              genre='新闻', image='test image1', is_deleted=0, is_published=1)
        Notice.objects.create(content='test content', title='test title',
                              genre='公告', image='test image', is_deleted=0, is_published=0)
        Notice.objects.create(content='test content2', title='test title2',
                              genre='类型', image='test image2', is_deleted=1, is_published=0)

    def handle(self, *args, **options):
        print('creating test_data...')
        if settings.DEV_MODE:
            self.create_test_user()
            self.create_test_pankou()
            self.create_test_notice()
