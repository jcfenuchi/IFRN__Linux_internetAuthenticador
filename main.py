from streamlit.web import cli

if __name__ == '__main__':
    cli.main_run(['streamlit_main.py', '--server.port', '80'])
