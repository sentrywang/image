from common.utils import get_msg


class ErrorCode(Exception):
    def __init__(self, code, params=None):
        message = '{}: {}'.format(code, get_msg(code))
        self.code = code
        if params:
            self.err_msg = get_msg(code).format(**params)
        else:
            self.err_msg = None
        super().__init__(message)
