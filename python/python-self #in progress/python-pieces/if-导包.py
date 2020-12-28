
# if语句是可以控制是否导包的
if use_sentry:
    # from sentry_sdk import capture_exception
    from config import config_sentry