import re

from ratelimit.exceptions import Ratelimited
from raven.contrib.django.models import sentry_exception_handler
from rest_framework.exceptions import (
    NotAuthenticated,
    AuthenticationFailed,
    MethodNotAllowed,
    PermissionDenied
)
from rest_framework.views import exception_handler, APIView

from common.exceptions import ErrorCode
from common.loggerwrapper import logger
from common.permissions import (
    UserAuthRequired,
    StaffAuthRequired,
    AgentAuthRequired,
    AgencyAuthRequired,
    FirstClassAgencyAuthRequired,
)
from common.render import r
from myuser.models import UserProfile


def error_code_exception_handler(exc, context):
    if isinstance(exc, ErrorCode):
        return r(exc.code, err_msg=exc.err_msg)
    elif isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        print(exc)
        return r('USER_NOT_LOGGED_IN')
    elif isinstance(exc, MethodNotAllowed):
        return r('METHOD_NOT_ALLOWED')
    elif isinstance(exc, PermissionDenied):
        user = context['request'].user
        if re.match("CSRF Failed: ", exc.detail):
            return r('CSRF_FAILED')
        if isinstance(user, UserProfile) and user.is_banned:
            return r('USER_BANNED')
        else:
            return r('PERMISSION_DENIED')
    elif isinstance(exc, Ratelimited):
        return r('RATE_LIMITED')

    response = exception_handler(exc, context)
    if response is None:
        logger.exception(exc)
        sentry_exception_handler(request=context)
        return r('INTERNAL_ERROR')
    else:
        return response


class BaseView(APIView):
    post_params = []

    def initial(self, request, *args, **kwargs):
        super().initial(request, args, kwargs)

        if (request.method == 'POST' and self.post_params
                and not set(self.post_params).issubset(request.data.keys())):
            raise ErrorCode('INVALID_PARAMETERS')


class AuthBaseView(BaseView):
    """requires user login"""
    permission_classes = (UserAuthRequired,)


class StaffBaseView(BaseView):
    """requires staff login"""
    permission_classes = (StaffAuthRequired,)


class AgentBaseView(BaseView):
    """requires agent login"""
    permission_classes = (AgentAuthRequired,)


class AgencyBaseView(BaseView):
    """requires agent login"""
    permission_classes = (AgencyAuthRequired,)


class FirstClassAgencyView(BaseView):
    """requires agent login"""
    permission_classes = (FirstClassAgencyAuthRequired,)
