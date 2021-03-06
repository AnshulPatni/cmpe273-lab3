# cmpe273-lab3
**_Implementation of Connected UDP and Multicast UDP client-server connection_**

### Connected UDP
A connected UDP socket is slightly different from a standard one as it can only send and receive datagrams to/from a single address. However this does not in any way imply a connection as datagrams may still arrive in any order and the port on the other side may have no one listening. The benefit of the connected UDP socket is that it may provide notification of undelivered packages. This depends on many factors (almost all of which are out of the control of the application) but still presents certain benefits which occasionally make it useful.

Unlike a regular UDP protocol, we do not need to specify where to send datagrams and are not told where they came from since they can only come from the address to which the socket is ‘connected’.

### Multicast UDP
Multicast allows a process to contact multiple hosts with a single packet, without knowing the specific IP address of any of the hosts. This is in contrast to normal, or unicast, UDP, where each datagram has a single IP as its destination. Multicast datagrams are sent to special multicast group addresses (in the IPv4 range 224.0.0.0 to 239.255.255.255), along with a corresponding port. In order to receive multicast datagrams, you must join that specific group address. However, any UDP socket can send to multicast addresses.

As with UDP, with multicast there is no server/client differentiation at the protocol level. Our server example is very simple and closely resembles a normal listenUDP protocol implementation. The main difference is that instead of listenUDP, listenMulticast is called with the port number. The server calls joinGroup to join a multicast group. A DatagramProtocol that is listening with multicast and has joined a group can receive multicast datagrams, but also unicast datagrams sent directly to its address. The server in the example above sends such a unicast message in reply to the multicast message it receives from the client.