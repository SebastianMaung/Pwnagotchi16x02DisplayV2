import requests
import json
import random
import time
import gettext
import os
#if it works it works
def se(va):


    url = 'http://localhost:8666/api/v1/mesh/data'
    headers = {'Content-Type': 'application/json'}
    data = {'msg': str(va)}

    # Convert the data dictionary to a JSON string
    json_data = json.dumps(data)

    # Send the POST request
    response = requests.post(url, headers=headers, data=json_data)

def write1(d):
    se(d)
class Voice:
#    os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/1602.py")
#    os.system("python3 /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/customd.py")
    def __init__(self, lang):
        print("H")
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        print(str(translation))
#        write(str(translation))
        translation.install()
#        refresh()
        self._ = translation.gettext
    def custom(self, s):
        return s

    def default(self):
        return self._('ZzzzZZzzzzZzzz')
    def on_starting(self):
        write1('Hi, Im Pwnagotchi! Starting...')
        return random.choice([
            self._('Hi, I\'m Pwnagotchi! Starting ...'),
            self._('New day, new hunt, new pwns!'),
            self._('Hack the Planet!')])

    def on_ai_ready(self):
        write1('AI ready')
        return random.choice([
            self._('AI ready.'),
            self._('The neural network is ready.')])

    def on_keys_generation(self):
        write1('Generating keys, do not turn off ...')
        return random.choice([
            self._('Generating keys, do not turn off ...')])

    def on_normal(self):
        write1('...')
        return random.choice([
            '',
            '...'])

    def on_free_channel(self, channel):
        write1('Hey, '+str(channel)+' is free! Your AP will say thanks.')
        return self._('Hey, channel {channel} is free! Your AP will say thanks.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        write1('Reading logs...')
        if lines_so_far == 0:
            return self._('Reading last session logs ...')
        else:
            return self._('Read {lines_so_far} log lines so far ...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        write1('Im bored...')
        return random.choice([
            self._('I\'m bored ...'),
            self._('Let\'s go for a walk!')])

    def on_motivated(self, reward):
        write1('This is the best day of my life!')
        return self._('This is the best day of my life!')

    def on_demotivated(self, reward):
        write1('Bad day :/')
        return self._('Shitty day :/')

    def on_sad(self):
        write1('Im very sad...')
        return random.choice([
            self._('I\'m extremely bored ...'),
            self._('I\'m very sad ...'),
            self._('I\'m sad'),
            '...'])

    def on_angry(self):
        # passive aggressive or not? :D
        write1('Im mad at you!')
        return random.choice([
            '...',
            self._('Leave me alone ...'),
            self._('I\'m mad at you!')])

    def on_excited(self):
        write1('So many networks!!!')
        return random.choice([
            self._('I\'m living the life! Im having so much fun!'),
            self._('I pwn therefore I am.'),
            self._('So many networks!!!'),
            self._('I\'m having so much fun!'),
            self._('My crime is that of curiosity ...')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            write1('Hello '+str(peer.name)+', nice to meet you.'),
            return random.choice([
                self._('Hello {name}! Nice to meet you.').format(name=peer.name())])
        else:
            write1('Yo '+str(peer.name)+'! Sup?'),
            return random.choice([
                self._('Yo {name}! Sup?').format(name=peer.name()),
                self._('Hey {name} how are you doing?').format(name=peer.name()),
                self._('Unit {name} is nearby!').format(name=peer.name())])

    def on_lost_peer(self, peer):
        write1('Uhm... goodbye '+str(peer.name)+'.'),
        return random.choice([
            self._('Uhm ... goodbye {name}').format(name=peer.name()),
            self._('{name} is gone ...').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            write1(str(who)+' missed!'),
            self._('Whoops ... {name} is gone.').format(name=who),
            self._('{name} missed!').format(name=who),
            self._('Missed!')])

    def on_grateful(self):
        write1('I love my friends!'),
        return random.choice([
            self._('Good friends are a blessing!'),
            self._('I love my friends!')])

    def on_lonely(self):
        write1('Nobody wants to play with me ...'),
        return random.choice([
            self._('Nobody wants to play with me ...'),
            self._('I feel so alone ...'),
            self._('Where\'s everybody?!')])

    def on_napping(self, secs):
        write1('Sleeping for '+str(secs)+'s...'),
        return random.choice([
            self._('Napping for {secs}s ...').format(secs=secs),
            self._('Zzzzz'),
            self._('ZzzZzzz ({secs}s)').format(secs=secs)])

    def on_shutdown(self):
        write1('Good night!'),
        return random.choice([
            self._('Good night.'),
            self._('Zzz')])

    def on_awakening(self):
        return random.choice(['...', '!'])

    def on_waiting(self, secs):
        write1('Looking around for '+str(secs)+'s...'),
        return random.choice([
            self._('Waiting for {secs}s ...').format(secs=secs),
            '...',
            self._('Looking around ({secs}s)').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        write1('Hey '+str(what)+', lets be friends! ')
        return random.choice([
            self._('Hey {what} let\'s be friends!').format(what=what),
            self._('Associating to {what}').format(what=what),
            self._('Yo {what}!').format(what=what)])

    def on_deauth(self, sta):
        write1('Just decided that '+sta['mac']+' needs no WiFi!')
        return random.choice([
            self._('Just decided that {mac} needs no WiFi!').format(mac=sta['mac']),
            self._('Deauthenticating {mac}').format(mac=sta['mac']),
            self._('Kickbanning {mac}!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        write1('Cool, we got '+str(new_shakes)+' new handshakes!'),
        return self._('Cool, we got {num} new handshake{plural}!').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        write1('You have unread messages!'),
        return self._('You have {count} new message{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        write1('Oops, something went wrong ... Rebooting ...'),
        return self._("Oops, something went wrong ... Rebooting ...")

    def on_last_session_data(self, last_session):
        write1('Cannot get last session data...'),
        write1('Kicked '+str(last_session.deauthed)+' stations')
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            write1('Made >999 new friends')
            status += self._('Made >999 new friends\n')
        else:
            write1('Made '+str(last_session.associated)+' new friends')
            status += self._('Made {num} new friends\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            write1('Met 1 peer')
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            write1('Met '+str(last_session.peers)+' peers')
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'I\'ve been pwning for {duration} and kicked {deauthed} clients! I\'ve also met {associated} new friends and ate {handshakes} handshakes! #pwnagotchi #pwnlog #pwnlife #hacktheplanet #skynet').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            # sing
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
#hi

