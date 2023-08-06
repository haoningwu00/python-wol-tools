#!python3
# coding = utf-8

import argparse
import logging
import api

__VERSION__ = '1.0'
__APP_NAME__ = 'python-wol-tools'

__LOGGING_FORMAT = "%(levelname)s:[%(filename)s:%(lineno)s-%(funcName)s()] %(message)s"
_LOGGER = logging.getLogger(__name__)

APP_OPTIONS = {
    'console': False,
    'auto_start_wol_server': False
}


def parse_arg():
    parser = argparse.ArgumentParser(description='服务器网络唤醒工具')
    parser.add_argument('-c', '--console', action='store_true', default=False, help='控制台启动')
    parser.add_argument('-s', '--startserver', action='store_true', default=False, help='直接启动WOL服务器')
    options = parser.parse_args()

    global APP_OPTIONS
    APP_OPTIONS['console'] = True
    APP_OPTIONS['auto_start_wol_server'] = options.startserver

    _LOGGER.info(f'应用配置 : {APP_OPTIONS}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=__LOGGING_FORMAT)
    parse_arg()

    if APP_OPTIONS.get('auto_start_wol_server'):
        api.start_wol_server()
