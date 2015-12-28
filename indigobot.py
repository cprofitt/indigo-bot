# twisted imports
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

# system imports

# api imports
import commands
from modules.config import Config

def doCommand(self, msg):
	if 'quit' in msg.lower():
		self.quit('goodbye')

class IndigoBot(irc.IRCClient):
	server = 'chat.freenode.net'
	port = 6667

	def _get_nickname(self):
        	return self.factory.nickname
    	nickname = property(_get_nickname)

	def signedOn(self):
        	self.join(self.factory.channel)
       		print "Signed on as {}.".format(self.nickname)

	def joined(self, channel):
        	print("Joined %s." % channel)

	def privmsg(self, user, channel, msg):
		# handle input
		# test for admin
		if 'cprofitt' in user.lower():
			# admin sending
			senderNick = user.split('!', 1)[0]
			self.msg(channel, senderNick + " I am at your command!")
			if 'indigo-bot:' in msg.lower():
				doCommand(self, msg)
		else:
			self.msg(channel, "sorry, you are not authorized")

	def userLeft(self, user, channel):
		print("someone left the channel")


class IndigoBotFactory(protocol.ClientFactory):
	protocol = IndigoBot
	cfg = Config('indigo-bot.conf')
	SERVER = cfg.get_option('server', 'address')
	NICK = cfg.get_option('info', 'nickname')
	CHANNEL = cfg.get_option('server', 'channels')

	def __init__(self, channel=CHANNEL, nickname=NICK):
        	self.channel = channel
        	self.nickname = nickname

	def clientConnectionLost(self, connector, reason):
		if 'closed cleanly' in str(reason):
			print "yes, I closed cleanly"
			reactor.stop()
		else:
	        	print("Lost connection (%s), reconnecting." % reason)
			connector.connect()

	def clientConnectionFailed(self, connector, reason):
        	print("Could not connect: %s" % reason)
