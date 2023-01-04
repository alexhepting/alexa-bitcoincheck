import requests
import json

def lambda_handler(event, context):
    # Make a request to the CoinMarketCap API to retrieve the current Bitcoin price
    response = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/")
    data = response.json()
    price = data[0]['price_usd']
    
    # Return the price to Alexa
    return {
        'statusCode': 200,
        'body': json.dumps({
            'speech': f'The current Bitcoin price is ${price}',
            'displayText': f'The current Bitcoin price is ${price}'
        })
    }
