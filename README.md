# pwnagotchi1602displayv2

Replace /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py with the voice.py from here
Once that is done, move driver.py and 1602.py to a directory together
Run 1602.py to see if it works
If it does, you can make it start at boot using a number of ways
A simple way is to go to your plugins and just add an 'os.system("python3 /path/to/1602.py &")' somewhere good
But it's much better to 'cd /etc/systemd/system/'
Add a new service with 'sudo nano 1602disp.service'
And then add this:

[Unit]
Description=1602DisplayOnBoot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/1602.py/
WorkingDirectory=/path/to/your/script_directory/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target


Then run 'sudo systemctl enable 1602disp.service'
Then start it with 'sudo systemctl start 1602disp.service'
Now it'll run on boot! Enjoy!
