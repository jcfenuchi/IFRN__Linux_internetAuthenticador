import streamlit as st
from web_auth import Timer
import sys
from loguru import logger

class Stream_app():

    def page(self):
        st.write('Autenticador Automatico para o IFRN')
        login = st.text_input(label='Matricula')
        password = st.text_input(label='Senha', type='password')
        submit_button = st.button(label='Submit')
        self.time_process = {'timer': None, 'loged': False}
        def stop():
            logger.debug('Parando o Clocker no Codigo main')
            if self.time_process.get('timer') != None:
                self.time_process.get('timer').stop_timer()
                self.time_process.get('timer').clocker.join()
                self.time_process.update({'timer': None})
                logger.debug('Parando o Clocker no Codigo main')
                st.stop()

        if submit_button:
            self.time_process.update({'loged': True})
            st.write('Timer is running now, please click on button to Stop.')
            st.button(label='Stop timer', on_click=stop)
            if self.time_process.get('timer') == None:
                self.time_process.update({'timer':Timer({'Login':login, 'Password':password})})
                self.time_process.get('timer').start_timer()
                
Stream_app().page()