#!/usr/bin/python3
from rcon.source import Client
import time
from datetime import datetime, timedelta
import os
import sys

def main():
    with Client(os.environ['MCRCON_HOST'], int(os.environ['MCRCON_PORT']), passwd=os.environ['MCRCON_PASS']) as client:
        try:
            i = int(sys.argv[1])
        except:
            print('\033[31mError, argument must be an \033[31;1minteger.\033[0;0m')
            exit()
        oi = i
        client.run('bossbar set timer visible true')
        while i >= 1:
            client.run(f'bossbar set timer value {int(((i) / oi) * 100)}')
            client.run(f'bossbar set timer name {{"text":"Time left: {time.strftime("%M:%S",time.gmtime(i))}","color":"light_purple"}}')
            print(time.strftime("%M:%S",time.gmtime(i)))
            i -= 1
            time.sleep(1)
        client.run('title @a title {"text":"Time''s Up!","color":"yellow"}')
        client.run('title @a subtitle {"text":"Time to Judge!"}')
        client.run('bossbar set timer visible false')
        client.run('playsound minecraft:block.note_block.pling master @a ~ ~ ~ 100 1')
        print ('Time''s Up!')

if __name__ == '__main__':
    try:
        main()
    except:
        with Client(os.environ['MCRCON_HOST'], int(os.environ['MCRCON_PORT']), passwd=os.environ['MCRCON_PASS']) as client:
            client.run('bossbar set timer visible false')
            client.run('title @a title {"text":"Timer cancelled!","color":"yellow"}')
