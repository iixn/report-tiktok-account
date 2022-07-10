try:
  import requests, json, threading, random, signal, sys
except:
  import os
  os.system("pip install requests")
  
def hand_signal(signal, frame):
  print("\033[1;33mBye")
  sys.exit()

signal.signal(signal.SIGINT, hand_signal)

username = input('\033[1;34m [ ? ] Username: ')
threads = int(input('\033[1;34m [ ? ] Threads: '))
countReport = 0

userId  = ""
secuId  = ""

def getInfo():
  header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Cookie": "msToken=zgbEqIjfSC7M7QdTTpHDkpWLtnY4JnK22HiSE1iHCRGBBYY_36Gm-gMDqyGLBjpPE2svzjVPNGWyMFYUUEBwmGkr5y2qQuKmfjfTh0i2hfOsb_B7jfDrbd9a4IhjMLPyUIRNIZLqzG6PldNNXA=="
  }
  url = f"https://www.tiktok.com/api/user/detail/?device_id=7098862702289995269&uniqueId={username}"
  data = requests.get(url, headers=header).json()["userInfo"]["user"]

  global userName
  userName = data["uniqueId"]
  userId = data["id"]
  secuId = data["secUid"]

  for thread in range(threads):
    threading.Thread(target=report()).start()

def report():
  while True:
    head =  {
      "user-agent": "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    }

    global countReport

    if "Thanks for your feedback" in requests.get(f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=TK&channel=tiktok_web&current_region=TK&device_id={random.randint(1000000000000000000, 9999999999999999999)}&lang=en&nickname={userName}&object_id=76493735542&os=onlp&owner_id={userId}&reason=317&region=TK&report_type=user&secUid={secuId}&target={userId}&tz_name=Tekky%2FOnlp', headers=head).text:
      countReport += 1
      print(f'\033[1;32m [ * ] Successfully reported ({countReport})')
    else:
      print('\033[1;31m [ * ] Failed to report')


if __name__ == '__main__':
  getInfo()
