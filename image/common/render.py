import datetime
import json
from decimal import Decimal

from django.http import HttpResponse

from common.utils import get_msg, convert_to_timestamp_from_datetime, convert_to_timestamp_from_date


def build_response(err_code, data=None, err_msg=None):
    resp = {
        'code': err_code,
        'msg': err_msg if err_msg else get_msg(err_code),
    }
    if data is not None:
        resp['data'] = data
    return resp


def my_render_json_to_response(err_code, data=None, sort_keys=False, err_msg=None):
    content = json.dumps(build_response(err_code, data, err_msg),
                         sort_keys=sort_keys, cls=MyJsonEncoder)
    return HttpResponse(content, content_type='application/json')


class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # noinspection PyTypeChecker
            return float(obj)
        elif isinstance(obj, datetime.datetime):
            return convert_to_timestamp_from_datetime(obj)
        elif isinstance(obj, datetime.date):
            return convert_to_timestamp_from_date(obj)

        return super().default(obj)


r = my_render_json_to_response
