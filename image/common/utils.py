import datetime
import re
import secrets
import string
import time
from decimal import Decimal
from math import ceil, trunc
from typing import Union, Iterable, Tuple, List, Dict, Any

from django.db.models import QuerySet

from common import errmsgs


def generate_code(length=6, use_base56=False):
    if use_base56:
        # noinspection SpellCheckingInspection
        alphabet = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    else:
        alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def generate_code_upper_base56(length=6):
    alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def get_msg(code):
    """获取错误码对应的消息"""
    return getattr(errmsgs, code, getattr(errmsgs, 'UNKNOWN_CODE'))


def remove_all_spaces(string_):
    return re.sub(r'\s+', '', string_)


def fmt_datetime_str(date, with_seconds=False):
    """format a datetime object to str"""
    if not date:
        return ''

    fmt = '%Y-%m-%d %H:%M'
    if with_seconds:
        fmt += ':%S'

    return date.strftime(fmt)


def fmt_date_str(date):
    """format date object to display"""
    if not date:
        return ''
    return date.strftime('%Y-%m-%d')


def convert_to_timestamp_from_datetime(dt: datetime.datetime):
    return int(dt.timestamp())


def convert_to_timestamp_from_date(dt: datetime.date):
    return int(time.mktime(dt.timetuple()))


def convert_timestamp_to_datetime_object(timestamp: Union[int, str, float]) -> datetime.datetime:
    """把时间戳转换为datetime对象
    :param timestamp: 大于0的数
    :return: datetime.datetime

    当前时间戳：1,500,363,867  (2017-07-18 15:44:27)
    10位整数能够表示的最大日期为：2286-11-21 01:46:39
    因此，如果传入的数字位数大于10位，将其除以多余的位数，从而转为符合当前时间的数字
    """
    timestamp = float(timestamp)
    digits = len(str(int(timestamp)))
    extra_digits = digits - 10
    if extra_digits > 0:
        timestamp /= 10 ** extra_digits
    return datetime.datetime.fromtimestamp(timestamp)


def fmt_timestamp_to_datetime_str(timestamp: Union[int, str, float], fmt='%Y-%m-%d %H:%M:%S') -> str:
    dt = convert_timestamp_to_datetime_object(timestamp)
    return dt.strftime(fmt)


def get_request_header(request, name):
    """获取请求头部某一个字段"""
    return request.META.get(name, '')


def get_client_ip(request):
    x_forwarded_for = get_request_header(request, 'HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = get_request_header(request, 'REMOTE_ADDR')
    return ip


def get_queryset_values(qs: QuerySet, fields: Iterable[str],
                        rename_fields: Iterable[Tuple[str, str]]=()) -> List[Dict]:
    """
    返回 query_set 的一些字段的值
    :param qs: query_set
    :param fields: 需要的字段
    :param rename_fields: 字段名重命名
    :return: List[Dict]

    example:
    >>> from myuser.models import UserProfile
    >>> qs = UserProfile.objects.all()
    >>> fields = ('email', 'uid')
    >>> rename_fields = (('uid', 'userId'),)
    >>> get_queryset_values(qs, fields, rename_fields)
    """
    result = qs.values(*fields)
    for x in result:
        for name, rename in rename_fields:
            x[rename] = x.pop(name)
    return list(result)


def get_flat_values_list(qs: QuerySet, field: str) -> List[Any]:
    """获取 QuerySet 中某个字段值的列表

    example:
    >>> from myuser.models import UserProfile
    >>> emails = get_flat_values_list(UserProfile.objects.all(), 'email')
    """
    return list(qs.values_list(field, flat=True))


def paginate(qs, page, page_size=20):
    total_records = qs.count()
    total_pages = ceil(total_records / page_size)  # type: int
    page = max(min(page, total_pages), 1)

    start = (page - 1) * page_size
    end = start + page_size

    qs = qs[start:end]

    return qs, page, total_pages


def is_expired(dt):
    return datetime.datetime.now() > dt


def truncate(number: Decimal, digits: Decimal) -> Decimal:
    """将小数点第N位之后的数据舍去"""
    number = float(number)
    number = Decimal(str(number))
    digits = Decimal(digits)
    stepper = pow(Decimal('10.0'), digits)
    return trunc(stepper * number) / stepper


def round2(number) -> Decimal:
    """将小数点第二位之后的数据舍去

    example:
    >>> round2(0.992)
    >>> 0.99
    """
    result = truncate(number, Decimal('2'))
    return Decimal(str(result))


def check_odds(bet_amounts):
    from match_bet.models import WIN_RATIO
    total = sum(bet_amounts)

    result = []
    for bet_amount in bet_amounts:
        odds = round2((total - bet_amount) * WIN_RATIO / bet_amount + 1)
        result.append(odds)

    return result
