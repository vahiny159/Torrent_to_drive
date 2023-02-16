from google.colab import drive
drive.mount('/content/drive/')
%cd '/content/drive/My Drive/Downloads/'
!add-apt-repository ppa:qbittorrent-team/qbittorrent-stable -y
!apt install qbittorrent-nox
TOKEN = "1rtb3jOAvQt6yg3FmsGM9Vv2l2x_4eAdaivESTBH5uJMKV9Kc"

def install_ngrok():
    import os
    from zipfile import ZipFile
    from urllib.request import urlretrieve
    
    url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
    urlretrieve(url, 'ngrok-amd64.zip')
    
    with ZipFile('ngrok-amd64.zip', 'r') as zip_ref:
        zip_ref.extractall('/usr/local/bin/')
    os.chmod('/usr/local/bin/ngrok', 0o755)
    os.unlink('ngrok-amd64.zip')

install_ngrok()
if TOKEN != "":
    !ngrok authtoken $TOKEN 
import threading
import time
import requests
import json
import subprocess

def torrent(port):
    command = subprocess.Popen(['qbittorrent-nox', f'--webui-port={port}'])

def ngrok(port):
    
    ngrok_cmd = subprocess.Popen(['ngrok', 'http', str(port)])    
    localhost_url = "http://localhost:4040/api/tunnels"

    time.sleep(1)
    tunnel_url = requests.get(localhost_url).text
    json_data = json.loads(tunnel_url)

    tunnel_url = json_data['tunnels'][0]['public_url']
    tunnel_url = tunnel_url.replace("https", "http")
    print('Running at localhost: ' + str(port))
    print(tunnel_url)

if __name__ == '__main__':
    
    port = 9999

    thread_torrent = threading.Thread(target = torrent, args=(int(port),))
    thread_ngrok = threading.Thread(target = ngrok, args=(int(port),))

    thread_torrent.start()
    print('Torrent server started!')

    time.sleep(5)
    print('Establishing secure connection!')
    
    thread_ngrok.start()
    print('Secure connection established...')
    print('Username: admin')
    print('password: adminadmin')      
    
    thread_ngrok.join()
    thread_torrent.join()


import requests
from IPython.display import clear_output
import time

while True:
    try:
        r = requests.get("http://www.google.com")
        clear_output(wait=True)
        print("Connected!")
    except:
        clear_output(wait=True)
        print("Not connected!")
    time.sleep(600)
