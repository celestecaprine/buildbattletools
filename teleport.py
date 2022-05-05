#!/usr/bin/python3
from rcon.source import Client
import sys
import os
import re
from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()

arenas = {
"A1": "383 -60 126",
"A2": "383 -60 94",
"A3": "383 -60 62",
"A4": "383 -60 30",
"B1": "415 -60 126",
"B2": "415 -60 94",
"B3": "415 -60 62",
"B4": "415 -60 30"
}
def main():
    try:
        playername = sys.argv[1]
        arenanum = sys.argv[2]
        with Client(os.environ['MCRCON_HOST'], int(os.environ['MCRCON_PORT']), passwd=os.environ['MCRCON_PASS']) as client:
            client.run(f'tp {playername} {arenas.get(arenanum)}')
    except:
        with Client(os.environ['MCRCON_HOST'], int(os.environ['MCRCON_PORT']), passwd=os.environ['MCRCON_PASS']) as client:
            playerlist = re.sub("^[^:]*: ", "", client.run('list')).split((", "))
            playertotp = fzf.prompt(playerlist, '--reverse')
            arenasel = fzf.prompt(list(arenas.keys()), '--reverse')
            arenaselcoords = arenas.get(arenasel[0])
            print(f'TPing {playertotp[0]} to Arena {arenasel[0]}: {arenaselcoords}')
            result = client.run(f'tp {playertotp[0]} {str(arenaselcoords)}')
            print(result)

if __name__ == '__main__':
    main()
