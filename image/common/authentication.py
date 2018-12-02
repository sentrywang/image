from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """对于继承 BaseView 的 View，不检查 csrftoken
    用法：
    >>> from common.views import BaseView
    >>> class LogoutView(BaseView):
    >>>    authentication_classes = (CsrfExemptSessionAuthentication,)
    >>>    def post(self, request):
    >>>        pass
    """

    def enforce_csrf(self, request):
        request.csrf_processing_done = True
        return super().enforce_csrf(request)
