from bittrex.bittrex import Bittrex, API_V1_1
my_bittrex = Bittrex(None, None, api_version=API_V1_1)  # or defaulting to v1.1 as Bittrex(None, None)


print(my_bittrex.get_markets())