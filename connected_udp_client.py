from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 8006

        self.transport.connect(host, port)
        print ("now we can only send to host %s port %d" % (host, port))
        self.transport.write("Hello World".encode())

    def datagramReceived(self, data, host):
        print ("received %r from %s" % (data.decode(), host))

    def connectionRefused(self):
        print ("No one listening")

reactor.listenUDP(0, Helloer())
reactor.run()