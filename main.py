import time
from datetime import datetime
from cleaner import clean


if __name__ == '__main__':
    while True:
        try:
            print('{}: Чистка обсуждений начата'.format(datetime.now()))
            clean()
            print('{}: Чистка обсуждений завершена\n'.format(datetime.now()))
            time.sleep(60*60)
        except Exception as err:
            print(err)
            time.sleep(10)
