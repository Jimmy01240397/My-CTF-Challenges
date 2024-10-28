ip -4 route del default
ip -4 route add default via 10.10.2.1 dev eth0

chown -R frr:frr /etc/frr
service frr start
service ssh start
sleep infinity
