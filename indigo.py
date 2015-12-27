from twisted.internet import reactor
from indigobot import IndigoBotFactory

factory = IndigoBotFactory()
reactor.connectTCP(factory.protocol.server, factory.protocol.port, factory)
reactor.run()
