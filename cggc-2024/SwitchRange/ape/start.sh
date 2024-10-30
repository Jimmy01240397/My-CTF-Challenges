ip link add internalvrf type vrf table 100
ip link set internalvrf up
ip link set dev eth3 master internalvrf

ip link add clientvrf type vrf table 200
ip link set clientvrf up
ip link set dev eth1 master clientvrf
ip link set dev eth2 master clientvrf

ip -4 addr flush dev eth0
ip -4 route del default
ip -6 route del default
ip -4 route del default vrf clientvrf
ip -6 route del default vrf clientvrf

ip -4 route add default via 10.10.0.254 dev eth1 vrf clientvrf

iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE
iptables -t nat -A PREROUTING -i eth1 -p tcp -m tcp --dport $PORT -j DNAT --to 192.168.100.1

chown -R frr:frr /etc/frr
service frr start
service ssh start
sleep infinity
