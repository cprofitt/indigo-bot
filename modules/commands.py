# twisted imports
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

# modules
from modules.config import Config

# load configuration
cfg = Config('indigo-bot.conf')
admin = cfg.get_option('admin', 'address')

# bot commands
def doCommand(self, user, channel, msg):
	# handle input
	senderNick = user.split('!', 1)[0]
	# test for admin
	if 'cprofitt' in user.lower():
		# admin sending
		self.msg(channel, senderNick + " I am at your command!")
		if 'indigo-bot:' in msg.lower():
			botCommand(self, msg)

	# send an message to private channel
	elif 'cprofitt:' in msg.lower():
		sendAlert(self, senderNick, channel, msg)
	else:
		self.msg(channel, "sorry, you are not authorized")	

# command codes
def botCommand(self, msg):
	if 'quit' in msg.lower():
		self.quit('goodbye')

def sendAlert(self, sender, channel, msg):
	self.msg('cprofitt', sender + ": " + channel + " - " + msg )
