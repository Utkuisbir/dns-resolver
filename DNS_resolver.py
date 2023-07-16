import dns.resolver
import time
import datetime
import itertools
import argparse
parser = argparse.ArgumentParser(
    description="This python code has written to verify connected AP resolving DNS's of hostnames from dictionary every second."
)
parser.add_argument('--time', '-t', type=int,
                    required=False,default=1, help='lengh of test run as hour')
args = parser.parse_args()
test_length_hour=args.time * 60 * 60
hostnames = (
"www.facebook.com",
"www.twitter.com",
"www.instagram.com",
"www.baidu.com",
"www.wikipedia.org",
"www.yandex.ru",
"www.yahoo.com",
"www.whatsapp.com",
"www.tiktok.com",
"www.amazon.com",
"www.openai.com",
"www.live.com",
"www.reddit.com",
"www.linkedin.com",
"www.netflix.com",
"www.office.com",
"www.yahoo.co.jp",
"www.bing.com",
"www.twitch.tv"
)
def resolve_dns(hostname):
    try:
        result = dns.resolver.query(hostname, 'A')
        ip_address = result[0].to_text()
        return ip_address
    except dns.resolver.NXDOMAIN:
        print("Hostname not found.")
        return None
    except dns.resolver.NoAnswer:
        print("No DNS records found for the hostname.")
        return None
    except dns.exception.DNSException as err:
        print("DNS resolution failed:", err)
        return None
    
if __name__ == "__main__":
    hostname_cycle = itertools.cycle(hostnames)
    for _ in range(test_length_hour):
        hostname = next(hostname_cycle)
        ip_address = resolve_dns(hostname)
        if ip_address:
            print("Hostname:", hostname)
            print("IP Address:", ip_address)
            time.sleep(1)
        else:
            now = datetime.datetime.now()
            now_as_string = now.strftime("%Y-%m-%d %H:%M:%S")
            with open("Errors.txt","a") as file:
                unresolved = now_as_string + "   " + hostname + "\n"
                file.write(unresolved)