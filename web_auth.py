from playwright.sync_api import sync_playwright
import time as t
from sys import argv
from icmplib import ping as icmp_ping
from re import findall

from loguru import logger
from threading import Thread, Event
from toml import load as load_toml
from time import sleep

class IFRN_AUTENTICATOR:
    def __init__(self,login,password):
        self.login = login
        self.password = password
    
    def autenticate(self):
        logger.debug('Iniciando a Autenticação.')
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_context(ignore_https_errors=True)
            page = page.new_page()
            page.goto(f'https://autenticacao-cnat.ifrn.local:6082/php/uid.php?vsys=1&rule=4')
            page.locator('[name=user]').fill(self.login)
            t.sleep(1.5)
            page.locator('[name=passwd]').fill(self.password)
            t.sleep(1.5)
            page.locator('[name=ok]').click()
            t.sleep(3)
            if findall(r'<b>User Authenticated</b>', page.content()):
                logger.debug('Autenticação bem sucedida.')
            else:
                logger.warning('Autenticação falhou.')
                page.close()
                browser.close()

            page.close()
        t.sleep(1)

class Timer:
    def __init__(self, data):
        self.event = Event()
        self.clocker = None
        self.data = data

        
    def start_timer(self):
        logger.debug(f'Iniciando o Timer')
        self.clocker = Thread(target=self.timer_handle)
        self.clocker.start()

    def timer_handle(self):
        while True:
            if self.event.is_set(): logger.debug('Event is set exiting of loop');break
            logger.debug('Iniciando Ping para google.com')
            ping = icmp_ping('google.com', count=5, interval=0.2)
            if ping.is_alive:
                logger.debug('Ping bem sucedido')
            elif not ping.is_alive:
                logger.debug('Ping falhou, Iniciando autenticação.')
                IFRN_AUTENTICATOR(self.data['Login'], self.data['Password']).autenticate()

            with open('config.toml', 'r') as conf: config = load_toml(conf)
            timeout = config.get('timeConfig').get('checkTimeout')
            logger.debug(f'Esperando Timeout de {timeout} segundos terminar.')

            sleep(timeout)
        logger.debug(f'Thread Finalizada')

    def stop_timer(self):
        logger.debug(f'Parando o Timer')
        self.event.set()







if __name__ == '__main__':
    timer = Timer({'Login':'', 'Password': ''})
    timer.start_timer()
    timer.stop_timer()