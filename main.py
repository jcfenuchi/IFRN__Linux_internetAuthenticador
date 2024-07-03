import streamlit as st
from web_auth import Timer


login = st.text_input(label='Login')
password = st.text_input(label='Password', type='password')
submit_button = st.button(label='Submit')

if submit_button:
    print(login,password)
    print(type(login), type(password))
    st.write(f'Login: {login}')
    st.write(f'Password: {password}')

    timer = Timer({'Login':login, 'Password':password})
    timer.start_timer()
    
    stop = st.button(label='Stop timer')
    if stop:
        timer.stop_timer()