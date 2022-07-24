from rich import print as rprint
from threading import Thread
import pingparsing

PING_COUNT = 1
ping_parser = pingparsing.PingParsing()

def ping(host):
    """
    Ping a host and return the response time.
    """
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = PING_COUNT

    # rprint(f"Pinging {host}...")
    response = ping_parser.parse(transmitter.ping()).as_dict()
    # rprint(response)

    rprint(f"{host} responded in {response['rtt_avg']}ms")
    return response["rtt_avg"]


Thread(target=ping, args=("8.8.4.4",)).start()
Thread(target=ping, args=("vpn.jalasoft.com",)).start()
Thread(target=ping, args=("svr3.bahai.org.br",)).start()
