from twisted.internet import reactor
from indigobot import MyBotFactory

factory = MyBotFactory()
reactor.connectTCP(factory.protocol.server, factory.protocol.port, factory)
reactor.run()
