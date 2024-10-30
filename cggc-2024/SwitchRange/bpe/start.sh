ip link add internalvrf type vrf table 100
ip link set internalvrf up
ip link set dev eth3 master internalvrf

ip link add clientvrf type vrf table 200
ip link set clientvrf up
ip link set dev eth0 master clientvrf
ip link set dev eth2 master clientvrf

ip -6 addr flush dev eth0
ip -4 addr flush dev eth1
ip -4 route del default
ip -6 route del default
ip -4 route del default vrf clientvrf
ip -6 route del default vrf clientvrf

ip -4 route add default via 10.10.0.254 dev eth0 vrf clientvrf

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

chown -R frr:frr /etc/frr
service frr start
service ssh start
sleep infinity
