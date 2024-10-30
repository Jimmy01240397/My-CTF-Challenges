ip link add internalvrf type vrf table 100
ip link set internalvrf up
ip link set dev eth3 master internalvrf

ip -6 addr flush dev eth0
ip -4 addr flush dev eth1
ip -4 addr flush dev eth2
ip -4 route del default
ip -6 route del default
ip -4 route del default vrf internalvrf
ip -6 route del default vrf internalvrf

ip -4 route add default via 10.10.0.254 dev eth0

ip link add tostuix type wireguard
wg setconf tostuix /etc/wireguard/tostuix.conf
ip link set tostuix up
ip addr add 2407:9240:3100:efff::1/127 peer 2407:9240:3100:efff::/127 dev tostuix
ip addr add fe80::13a8:258e:815c:e8b6/64 dev tostuix

chown -R frr:frr /etc/frr
service frr start
service ssh start
sleep infinity
