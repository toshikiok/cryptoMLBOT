import threading
import sys
import os
import traceback
import time
import psutil

class PanicManager:
   def __init__(self, logger=None):
       self.monitors = {}
       self.logger = logger
       self.lock = threading.Lock()
       self.thread = threading.Thread(target=self.run)
       self.thread.start()

   def register(self, tag=None, start_time=None, interval=None):
       self.logger.debug('panic_manager register tag {} start_time {} sec interval {} sec'.format(tag, start_time, interval))
       with self.lock:
           self.monitors[tag] = {
               'start_at': time.time(),
               'ping_at': None,
               'start_time': start_time,
               'interval': interval
           }

   def ping(self, tag=None):
       with self.lock:
           self.monitors[tag]['ping_at'] = time.time()

   def panic(self):
       restart_program(logger=self.logger)

   def run(self):
       while True:
           self.logger.debug('panic_manager loop')
           now = time.time()
           with self.lock:
               for tag in self.monitors:
                   monitor = self.monitors[tag]
                   if monitor['ping_at']:
                       if now - monitor['ping_at'] > monitor['interval']:
                           self.logger.error('{} ping delayed. restarting'.format(tag))
                           self.panic()
                   else:
                       if now - monitor['start_at'] > monitor['start_time']:
                           self.logger.error('{} start delayed. restarting'.format(tag))
                           self.panic()
           time.sleep(5)

# https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself
def restart_program(logger=None):
   try:
       p = psutil.Process(os.getpid())
       for f in p.open_files() + p.connections():
           os.close(f.fd)
   except Exception as e:
       logger.error('exception ' + traceback.format_exc())
   python = sys.executable
   os.execl(python, python, *sys.argv)

   
   
   # 初期化
# start_time: 最初の報告までの猶予(秒)
# interval: 2回目以降報告までの猶予(秒)
# tag: 監視対象を表す任意のtag

self.panic_manager = PanicManager(logger=logger)
self.panic_manager.register(tag='trader', start_time=5 * 60, interval=60)


# 定期的に生存報告
# ok: 正常かどうか。ボットごとにカスタマイズ

if ok:
    self.panic_manager.ping('trader')
      
      
      #Docker上のbotを監視・再起動する方法
      
      
      #前提と動作
#Dockerのlogを監視し，logを出力しなくなったらコンテナを再起動します．
#Dockerを使っていること
#定期的に，logを出力するようになっていること（走らせているプログラムが，定期的に何かprintすれば良いです）
#「botが停止している⇔logが出力されない」であること
      
import subprocess
import time
from datetime import datetime

CONTAINER_ID  = '監視するコンテナIDを入れてください'

print('start:' + str(datetime.now()))
while True:
    process = (subprocess.Popen('docker logs ' + CONTAINER_ID + ' --since="1m"', stdout=subprocess.PIPE,
                           shell=True).communicate()[0]).decode('utf-8')
    if not process:
        process = (subprocess.Popen('docker restart ' + CONTAINER_ID, stdout=subprocess.PIPE,
                            shell=True).communicate()[0]).decode('utf-8')
        print('restart docker:' + str(datetime.now()))
    time.sleep(60)
   
   
   
   
   
