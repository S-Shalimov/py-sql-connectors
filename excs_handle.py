import traceback


def handle_db_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            tb = traceback.extract_tb(ex.__traceback__)
            error_message = f'error: {tb[1][1]}: def {tb[1][2]}(): {tb[1][3]}: ' + str(ex)
            # logging
    return wrapper