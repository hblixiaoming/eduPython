import logging


def fun():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        logging.exception(e)
        raise e
    finally:
        print('finally...')
    print('END')

    pass


fun()
