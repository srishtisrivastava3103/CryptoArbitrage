import requests
import math

def getDataFromAPI():
    root_url = "https://api.binance.com/"

    exchangeInfo_endpoint = "api/v1/exchangeInfo"
    exchangeInfo_response = requests.get(root_url+exchangeInfo_endpoint)
    exchangeInfo_response = exchangeInfo_response.json()
    ticker_price_endpoint = "api/v3/ticker/price"
    ticker_price_response = requests.get(root_url+ticker_price_endpoint).json()
    # print((ticker_price_response))
    price_list = {}
    for index in range(len(ticker_price_response)) :
        baseAsset = exchangeInfo_response['symbols'][index]['baseAsset']
        quoteAsset = exchangeInfo_response['symbols'][index]['quoteAsset']
        price = -1*math.log(float(ticker_price_response[index]['price']))
        if quoteAsset in price_list:
            price_list[quoteAsset].append([baseAsset,price])
        else:
            price_list[quoteAsset] = [[baseAsset,price]]
    print(price_list)

getDataFromAPI()