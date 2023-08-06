import binascii
import socket
import logging

_LOGGER = logging.getLogger(__name__)


def normalization_mac(mac_addr: str):
    n_mac = ""
    if len(mac_addr) == 12:
        n_mac = mac_addr
    elif len(mac_addr) == 17:
        n_mac = mac_addr.replace(mac_addr[2], "")
    else:
        _LOGGER.warn('MAC地址输入有误')

    return n_mac


def send_magic_pack(n_mac: str):
    data = 'FF' * 6 + n_mac * 16
    send_data = binascii.unhexlify(data)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        sock.sendto(send_data, ('255.255.255.255', 9))
        return 1
    except Exception as err:
        _LOGGER.error(f'出现错误 : {err}')
        return -1
