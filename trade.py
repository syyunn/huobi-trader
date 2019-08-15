import argparse

import huobi
from huobi.model import *
import utils

# Set arguments to be input from the entry point
parser = argparse.ArgumentParser()
parser.add_argument('-api_key', type=str, required=True)
parser.add_argument('-secret_key', type=str, required=True)

args = parser.parse_args()

request_client = huobi.RequestClient(api_key=args.api_key,
                                     secret_key=args.secret_key)

# Get the timestamp from Huobi server
server_timestamp = str(request_client.get_exchange_timestamp())[:10]  # Unix
server_time = utils.unix2datetime(int(server_timestamp))

# Set API Keys and Authenticating Secret Keys
ticker = "btcusdt"

order_id = request_client.create_order(ticker,
                                       AccountType.SPOT,
                                       OrderType.BUY_LIMIT,
                                       amount=1.0,
                                       price=1.0)

order_status = request_client.get_order("symbol", order_id)


if __name__ == "__main__":
    pass
