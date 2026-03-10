import requests
import sys


try:
    if len(sys.argv) != 2:
        sys.exit('Usage: ... bitcoin.py {amount}')
    usd = float(sys.argv[1])
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except IndexError:
    sys.exit('Usage: ... bitcoin.py {amount}')
except ValueError:
    sys.exit('Usage: ... bitcoin.py {amount}')
except requests.RequestException:
    sys.exit('Usage: ... bitcoin.py {amount}')
