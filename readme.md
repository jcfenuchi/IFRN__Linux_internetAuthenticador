### This code verify your conection state and authenticate in the IFRN, on linux.

```bash
sudo make
sudo python3 main.py
```

```toml
# you can set the timeout in config.toml like: 
checkTimeout = 600
# obs this file is read every time when time is over.
# any exception is return the exception and put default 60 seconds as default value.
```