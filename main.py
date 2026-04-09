import logging
import time
from functools import partial

from faker_generator import FakerGenerator
from models.app_locale import AppLocale
from models.user import User
from utils.concurrency import multi_processing

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def print_result(users, running_time):
    logging.info(f'Generated {format(len(users))} unique users in {format(running_time)} seconds')


def gen_unique_users(locale: str, count: int) -> set[User] | None:
    # Generate unique users for the specified locale
    try:
        fg = FakerGenerator(locale=locale)
        unique_users = fg.gen_unique_users(count)
        return unique_users
    except Exception as e:
        raise Exception(f'Error generating users for locale {locale}: {e}')


def print_unique_user(locales: list[AppLocale], iter_count: int, core_count: int):
    tasks = []
    for locale in locales:
        f = partial(gen_unique_users, locale=locale.locale, count=iter_count)
        tasks.append(f)
    return multi_processing(tasks=tasks, max_workers=core_count)


if __name__ == "__main__":
    locales = [
        AppLocale(code='US', name='United States', locale='en_US'),
        AppLocale(code='FR', name='France', locale='fr_FR'),
        AppLocale(code='IT', name='Italy', locale='it_IT'),
        AppLocale(code='ES', name='Spain', locale='es_ES'),
        AppLocale(code='JP', name='Japan', locale='ja_JP'),
        AppLocale(code='RU', name='Russia', locale='ru_RU'),
        AppLocale(code='UK', name='United Kingdom', locale='en_GB'),
        AppLocale(code='CN', name='China', locale='zh_CN'),
        AppLocale(code='TW', name='Taiwan', locale='zh_TW'),
        AppLocale(code='VN', name='Vietnam', locale='vi_VN'),
        AppLocale(code='DE', name='Germany', locale='de_DE'),
        AppLocale(code='BR', name='Brazil', locale='pt_BR'),
        AppLocale(code='MX', name='Mexico', locale='es_MX'),
        AppLocale(code='IN', name='India', locale='en_IN'),
        AppLocale(code='ID', name='Indonesia', locale='id_ID'),
        AppLocale(code='BD', name='Bangladesh', locale='bn_BD'),
        AppLocale(code='NP', name='Nepal', locale='ne_NP'),
        AppLocale(code='KR', name='Korea', locale='ko_KR'),
        AppLocale(code='HU', name='Hungary', locale='hu_HU'),
    ]

    instances = [
        {
            'name': 't3.medium',
            'core': 1,
            'vcore': 2,
            'ram': 4,
            'price': 0.0528
        },
        {
            'name': 't3.xlarge',
            'core': 2,
            'vcore': 4,
            'ram': 16,
            'price': 0.2112
        },
        {
            'name': 't3.2xlarge',
            'core': 4,
            'vcore': 8,
            'ram': 32,
            'price': 0.4224
        }
    ]

    instance = instances[2]
    start_time = time.time()
    r = print_unique_user(locales=locales, iter_count=1_000_000, core_count=instance['core'])
    total_time_hour = ((time.time() - start_time) / 60 / 60)

    logging.info(
        f'Name: {instance['name']}, Total time: {total_time_hour} hours')
