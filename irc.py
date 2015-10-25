import socket
bot_owner = "QuyenVu"
nick = "quyen"
chan = "#cisdem"
sock = socket.socket()
sock.connect(("irc.foonetic.net",6667))
sock.send("USER " + nick + " 0 * :" + bot_owner + "\r\n")
sock.send("NICK " + nick + "\r\n")
while 1:
   data = sock.recv(512)
   print data
   if data[0:4] == "PING":
      sock.send(data.replace("PING", "PONG"))
   if data[0]!=':':
      continue
   if data.split(" ")[1] == "001":
      sock.send("MODE " + nick + " +B\r\n")
      sock.send("JOIN " + chan + "\r\n")
   elif data.split(" ")[1] == "PRIVMSG" and data.split(":")[2].startswith(nick):
      sock.send("PRIVMSG " + chan + " :Someone just spoke to me!\r\n")