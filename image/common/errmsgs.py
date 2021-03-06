OK = '成功'

UNKNOWN_CODE = '未知错误'
INTERNAL_ERROR = '内部错误'
INVALID_PARAMETERS = '参数错误'
CSRF_FAILED = 'csrf token 错误或已过期'
METHOD_NOT_ALLOWED = '方法不被允许'
USER_NOT_LOGGED_IN = '用户未登录或登录过期'
RATE_LIMITED = '请求太频繁，请稍候再试'
ERROR_404 = '404 Not Fount'
PERMISSION_DENIED = '您没有执行该操作的权限'
IN_CONSTRUCTION = '正在完善功能，请稍候再试'

INVALID_EMAIL = '邮箱格式错误'
INVALID_EMAIL_VERIFY_CODE = '邮箱验证码错误'
PASSWORD_NOT_STRONG = '密码强度太弱'
INVALID_USERNAME = '用户名格式错误'
WRONG_PASSWORD = '原密码错误'
USERNAME_USED = '用户名已被使用'
EMAIL_USED = '邮箱已被使用'
EMAIL_NOT_EXIST = '邮箱不存在'
EMAIL_NOT_VERIFIED = '邮箱未验证'
EMAIL_VERIFY_FAILED = '邮箱验证失败'
EMAIL_ALREADY_VERIFIED = '邮箱已验证'
EMAIL_VERIFY_TOKEN_EXPIRED = '激活链接已过期'
WRONG_CAPTCHA_CODE = '图形验证码错误'
WRONG_USERNAME_OR_PASSWORD = '用户名、邮箱或密码错误'
PASSWORD_NOT_MATCH = '两次输入的密码不一致'
AVATAR_INVALID = '头像格式错误'
RESET_PASSWORD_TOKEN_EXPIRED = '重置密码链接已过期'
ERROR_SAME_TEAM = '不能选择两个相同的战队'
INVALID_REFERRAL_CODE = '邀请码不存在，请输入有效的邀请码'
USER_BANNED = '您的账号已被封禁，请联系客服邮箱 support@1sportsfun.com 处理。'

INSUFFICIENT_BALANCE = '账户余额不足'
BET_CLOSED = '该场次比赛已封盘，不再接受下注'
INVALID_BET_AMOUNT = '只接受大于0的整数数额下注'
TOTAL_BET_AMOUNT_LIMIT_REACHED = '对不起，您在该比赛结果总下注量已超过限额'
NEW_USER_BET_AMOUNT_EXCEED_LIMIT = '未充值用户下注额超过限制'
ODDS_CHANGED = '该下注选项赔率发生了变化，请刷新页面后重新下注'

MATCH_ALREADY_SETTLED = '该场比赛已经结算'
PANKOU_ALREADY_SETTLED = '该盘口已经结算'
INVALID_MATCH_RESULT = '比赛结果设定参数错误'

BET_CLOSE_TIME_TOO_LATE = '封盘时间不能晚于比赛开始时间'
BET_CLOSE_TIME_TOO_EARLY = '封盘时间不能早于当前时间'
INVALID_LIVE_ROOM_INFO = '直播盘需提供直播房间号和直播URL'
INVALID_ODDS = '赔率不能同时大于1'
INVALID_FIXED_ODDS = '固定赔率的盘口，各赔率倒数之和应大于1'
EMPTY_OUTCOME_TITLE = '押注内容不能为空'
DUPLICATED_OUTCOME_TITLE = '同一盘口不能有两个相同的押注选项'
INVALID_PANKOU_RELATED_VALUE = '盘口关联值应为1-99的整数'
PANKOU_IDS_NOT_MATCH = '提交的盘口ID与数据库不匹配'
PANKOU_FIX_ODDS = '该比赛为浮动赔率，不能手动修改赔率'
HALF_OUTCOMES_NOT_2 = '赢半设置仅适用于有两个可能选项的盘口'
OUTCOME_CANNOT_ALL_BE_WINNERS = '盘口选项不能都是赢家'
INVALID_GAME_NAME = '游戏类型不存在'
INVALID_TOURNAMENT_NAME = '赛事不存在'

AGENCY_NOT_FOUND = '没有找到对应的代理'
WRONG_BONUS_TYPE = '输入的红利类型有误'
INVALID_BONUS_MULTIPLIER = '红利释放倍数应为1-99整数'
INVALID_BONUS_AMOUNT = '红利积分应为1-1000000整数'
DUPLICATED_BONUS_CODE = '红利码不能重复'
INVALID_BONUS_CODE = '无效的红利代码'
CURRENT_HAS_BONUS = '当前有正在生效的红利，请等待释放后再使用该代码兑换'
USER_HAS_ALREADY_COLLECTED_BONUS = '您已兑换过该红利，请勿重复兑换'
BONUS_AMOUNT_NOT_FURFILLED = '您当前红利流水不满足红利释放数额，暂时无法兑回USDT'
CHALLENGE_BONUS_MUST_OVER_50 = '挑战红利兑换需要至少50USDT'
CHALLENGE_REQUIRES_ZERO_BALANCE = '兑换挑战红利要求当前账户积分余额小于1'
CHALLENGE_REQUIRES_USER_AGENCY = '挑战红利仅限通过部分推广渠道注册用户享受'
CANNOT_CONVERT_FROM_USDT_WHILE_CHALLENGE_BONUS = '挑战红利生效期间不能兑换成积分'
USER_DOES_NOT_HAVE_CHALLENGE_BONUS = '用户当前没有生效的挑战红利'
INVALID_BONUS_BET_AMOUNT = '当前红利流水不满足释放条件'
USER_HAS_UNSETTLED_BET = '用户有尚未结算的下注单，请等待结算后再操作'

INVALID_USDT_WITHDRAW_ADDRESS = '请输入正确的提现地址'
INVALID_USDT_ADDRESS = '请输入正确的USDT地址'
WITHDRAW_ADDRESS_NOT_BOUND = '尚未绑定提现地址'
DO_NOT_BIND_DEPOSIT_ADDRESS = '请不要绑定系统分配的充值地址'
INVALID_WITHDRAW_AMOUNT = '提现金额不满足最低提现额要求'
INSUFFICIENT_USDT_BALANCE = '您账户的USDT余额不足'
USER_WITHDRAW_ALREADY_PROCESSED = '该笔用户提现已被处理'
INVALID_USDT_DEPOSIT_ADDRESS = '请检查输入的USDT充值地址'
WITHDRAW_ADDRESS_BOUND_TO_USER = '该地址已被其他用户绑定，请输入新的USDT地址'

INSUFFICIENT_USDT = '账户USDT余额不足'
INVALID_CONVERT_AMOUNT = '请输入大于0的数'
INVALID_USER_EMAIL = '找不到该邮箱对应的用户，请检查邮箱是否输入正确'

EMPTY_GAME_NAME = '游戏名称不能为空'

INVALID_COMMISSION_RATE = '请输入合理的返佣率'
INVALID_SECONDARY_COMMISSION_RATE = '二级代理返佣率不能超过您自己的返佣率'
WAIT_FOR_CHECKING = '提现金额超过50USDT，请耐心等待审核'
ALREADY_PROCESSED = '该笔提现已处理，请勿重复处理'
ONE_TIME_PER_DAY = 'USDT 提现每天限一次'
INSUFFICIENT_USDT_OR_BTC = '钱包USDT或BTC余额不足'
WITHDRAW_ERROR = '提现出现错误'

BALANCE_SHOULD_ABOVE_ZERO = '余额需大于0'
USER_DO_NOT_HAS_BONUS = '用户当前没有生效红利'

INVALID_NOTICE_CONTENT = '请输入公告内容'
INVALID_NOTICE_TITLT = '请输入公告标题'
INVALID_NOTICE_GENRE = '请输入公告类型'
