ip -4 route del default
ip -4 route add default via 192.168.100.254 dev eth0

python3 .
