#!/usr/bin/env python
# -*- coding: utf-8 -*-
# fullyautomatedluxuryastroturfing
# https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/powertrack-stream

from time import sleep
# from daemonize import Daemonize
import tweepy, time, sys, os
#from creds, political, bot
from creds import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)





#
# bot1 = new Bot('pierrerabhi')
# bot1.addtrigger('keyword','rabhi')
# bot1.addtrigger('user','@prabhi')
# ot1.addtrigger('followers','@prabhi')
# bot1.addreply('usul','https://youtube.com/...', 'Une petite video qui vous montre une autre facette de Pierre Rabhi', 'Un autre point de vue sur l\'ecologie !')
#
# addbot(bot1)


import io, json
# with io.open('bots.txt', 'rw', encoding='utf-8') as f:
  # f.write(json.dumps(data, ensure_ascii=False))

def main():
    f = open('bots.txt', 'rw')
    a = json.loads(f.read())
    print json.dumps(a)
    f.close

    print "Looping..."
    api.
        pass

main()

# daemon = Daemonize(app="test_app", pid=pid, action=main)
# daemon.start()
