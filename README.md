# pwnagotchi1602displayv2

Replace /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py with the voice.py from here
Once that is done, move driver.py and 1602.py to a directory together
Run 1602.py to see if it works
If it does, you can make it start at boot using a number of ways
A simple way is to go to your plugins and just add an os.system("python3 /path/to/1602.py &") somewhere good
