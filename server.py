# server.py

import socket                 
import queue
from flask import Flask, request
import os, sys, time 


class FileWatcher(object):
    def __init__(self, tailed_file):
        self.check_file_validity(tailed_file)
        self.tailed_file = tailed_file
        self.callback = sys.stdout.write

    def watch(self, s=1):
        with open(self.tailed_file) as file_:
            file_.seek(0,2)
            while True:
                curr_position = file_.tell()
                line = file_.readline()
                if not line:
                    file_.seek(curr_position)
                    time.sleep(s)
                else:
                    self.callback(line)

    def register_callback(self, func):
        self.callback = func

    def check_file_validity(self, file_):
        if not os.access(file_, os.F_OK):
            raise TailError("File '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("File '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("File '%s' is a directory" % (file_))

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message


port = 8087                # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind(('', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print (f'Server listening on port {port}')

client_list = []

def send_new_line(txt):
    for i in range(len(client_list)):
        client_list[i].send(txt.encode())


def last10Lines(filename):
    q = queue.Queue()
    size = 0
    n = 10
    lines = []

    with open(filename) as fh:
        for line in fh:
            q.put(line.strip())
            if size >= n:
                q.get()
            else:
                size += 1      

    for i in range(size):
        lines.append(q.get())
    return lines

while True:
    conn, addr = s.accept()     # Establish connection with client.
    client_list.append(conn)
    print ('Got connection from', addr)

    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = 'dummy_server_log.txt'
    lines = last10Lines(filename)
    for line in lines:
       conn.send(line.encode())
       print('Sent ',repr(line))

    print('Done sending')

    t = FileWatcher(filename)
    t.register_callback(send_new_line)
    t.watch(s=3)



