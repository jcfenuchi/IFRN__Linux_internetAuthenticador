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

# if you want create code as a process

create file bellow in /etc/systemd/syste/ifrn_auth.service
```toml
[Unit]
Description=ifrn_auth service https://github.com/jcfenuchi/IFRN__Linux_internetAuthenticador
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=3
User=root
WorkingDirectory=/home/jcfenuchi/IFRN__Linux_internetAuthenticador/
ExecStart=/usr/bin/python3 /home/jcfenuchi/IFRN__Linux_internetAuthenticador/main.py >/home/jcfenuchi/IFRN__Linux_internetAuthenticador/log.txt 2>&1


[Install]
WantedBy=multi-user.target
```
> OBS: you need change '/home/jcfenuchi/IFRN__Linux_internetAuthenticador/' To the folder with you have make the git clone.


use the comand to start a service!
```bash
# start service
service start ifrn_auth 

# check status
service status ifrn_auth
```

if status OK check https://localhost:PORT_SELECT_IN_MAIN_PY