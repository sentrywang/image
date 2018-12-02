import json
import traceback

from channels.generic.http import AsyncHttpConsumer
from django.conf import settings
from raven.contrib.django.models import sentry_exception_handler

from common.loggerwrapper import logger
from common.render import build_response, MyJsonEncoder
from myuser.models import UserProfile


# noinspection PyBroadException
class BaseAsyncHttpConsumer(AsyncHttpConsumer):
    async def check_permission(self):
        pass

    async def handle(self, body):
        try:
            await self.check_permission()
            await self.handle_request(body)
        except Exception:
            logger.error(traceback.format_exc())
            sentry_exception_handler()
            await self.send_json_response('INTERNAL_ERROR')

    async def handle_request(self, body):
        raise NotImplementedError(
            "Subclasses of AsyncHttpConsumer must provide a handle() method."
        )

    async def send_json_response(self, err_code, data=None, sort_keys=False, err_msg=None):
        content = json.dumps(build_response(err_code, data, err_msg),
                             sort_keys=sort_keys, cls=MyJsonEncoder)
        headers = [('Content-Type', 'application/json')]
        if settings.DEV_MODE:
            origin = dict(self.scope['headers']).get(b'origin')
            headers += [
                ('Access-Control-Allow-Credentials', 'true'),
                ('Access-Control-Allow-Origin', origin),
                ('Access-Control-Allow-Methods', 'DELETE, GET, OPTIONS, PATCH, POST, PUT'),
                ('Access-Control-Allow-Headers', ', '.join(settings.CORS_ALLOW_HEADERS)),
            ]
        await self.send_response(200, content.encode(), headers=headers)


class AuthAsyncHttpConsumer(BaseAsyncHttpConsumer):
    async def check_permission(self):
        user = self.scope['user']
        if not (user.is_authenticated and isinstance(user, UserProfile)):
            await self.send_json_response('USER_NOT_LOGGED_IN')

    async def handle_request(self, body):
        return await super().handle_request(body)
