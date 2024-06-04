from fastapi import FastAPI, HTTPException
import requests
import json

# TODO: Test Each Function and add Query parameters to Screener

# Endpoints I have access to
# Stock Price Change (Completed)
# Profile (Completed)
# Quote (Completed)
# Market Capitalization (Completed)
# Stock Screener (Add Parameters)
apikey = "7573e58029f1281198bb1d12ee0ed025"


def get_quote_order(symbol: str, apikey: str):
    url = f"https://financialmodelingprep.com/api/v3/quote-order/{symbol}?apikey={apikey}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")


# Add Query Parameters
def stock_screener(apikey: str, beta_max: str, beta_min: str, market_cap_max: str, market_cap_min: str, price_max: str,
                   dividend_min: str, sector: str, industry: str, country:str, exchange:str):
    url = (f"https://financialmodelingprep.com/api/v3/stock-screener?apikey={apikey}&betaMoreThan={beta_min}&" +
           f"betaLowerThan={beta_max}&marketCapMoreThan={market_cap_min}&marketCapLowerThan={market_cap_max}&" +
           f"priceLowerThan={price_max}&priceMoreThan=1&dividendMoreThan={dividend_min}&sector={sector}&" +
           f"Industry={industry}&Country={country}&exchange={exchange}&isActivelyTrading=true&isFund=false&limit=100")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")


def profile(symbol: str, apikey: str):
    url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={apikey}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")


def market_cap(symbol: str, apikey: str):
    url = f"https://financialmodelingprep.com/api/v3/market-capitalization/{symbol}?apikey={apikey}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")


def price_change(symbol: str, apikey: str):
    url = f"https://financialmodelingprep.com/api/v3/stock-price-change/{symbol}?apikey={apikey}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")


if __name__ == "__main__":

    stocks = ["AAPL", "NVDA", "GOOGL", "META", "TSLA", "NFLX", "MSFT", "INTC", "PANW", "AVGO"]
    myPortfolio = ["INSW", "GOOGL", "PERI", "BABA", "SEDG", "VALE", "KVYO", "UBS", "CQQQ", "RHHBY", "ON",
                   "REMX", "JFIN", "MT", "CHPT", "PYPL", "RIVN", "TWLO", "INTC"]
    PERatio = []

    # Stock Screener Code
    # Stock Screener Params Order
    # apikey, beta_max, beta_min:, market_cap_max, market_cap_min, price_max, dividend_min, sector, industry, country, exchange
    beta_max = "1.5"
    beta_min = "-1"
    market_cap_max = "50000000000"
    market_cap_min = "10000000000"
    price_max = "400"
    dividend_min = "0"
    # Sectors: ConsumerCyclical, Energy, Technology, Industrials, Financial Services, Basic Materials,
    # Communication Services, Consumer Defensive, Healthcare, Real Estate, Utilities,
    # Industrial Goods, Financial, Services, Conglomerates
    sector = "Industrials"
    # Industries: Autos, Banks, Banks Diversified, Software, Banks Regional, Beverages Alcoholic, Beverages Brewers, Beverages Non-Alcoholic, ..
    industry = ""
    # Countries: US, UK, MX, BR, RU, HK, CA, ..
    country = "US"
    exchange = "NASDAQ"
    screener = stock_screener("7573e58029f1281198bb1d12ee0ed025", beta_max, beta_min, market_cap_max, market_cap_min, price_max, dividend_min, sector, industry, country, exchange)
    exchange = "NYSE"
    screener += stock_screener("7573e58029f1281198bb1d12ee0ed025", beta_max, beta_min, market_cap_max, market_cap_min, price_max, dividend_min, sector, industry, country, exchange)
    for symbol in screener:
        print(symbol)
        quote = get_quote_order(symbol["symbol"], "7573e58029f1281198bb1d12ee0ed025")
        print(quote)
        if(quote[0]["pe"] != None ):
            PERatio.append((symbol["symbol"], quote[0]["pe"]))
    PEsort = sorted(PERatio, key=lambda PE: PE[1])
    for symbol in PEsort:
        print(symbol[0] + ": {}\n".format(symbol[1]))
        price_changes = price_change(symbol[0], "7573e58029f1281198bb1d12ee0ed025")
        print(f"{price_changes}\n")


    # singleStockPC = price_change("skyy","7573e58029f1281198bb1d12ee0ed025")
    # print(singleStockPC)
    # singleStockQuote = get_quote_order("skyy", "7573e58029f1281198bb1d12ee0ed025")
    # print(singleStockQuote)
    #
    # for symbol in stocks:
    #      data = get_quote_order(symbol, "7573e58029f1281198bb1d12ee0ed025")
    #      PERatio.append((data[0]["symbol"], data[0]["pe"]))
    #      print(json.dumps(data, indent=4, separators=(",", ": "), ensure_ascii=False))
    #
    # print("\n\n")
    #
    # for symbol in myPortfolio:
    #     data = get_quote_order(symbol, "7573e58029f1281198bb1d12ee0ed025")
    #     PERatio.append((data[0]["symbol"], data[0]["pe"]))
    #     # print(json.dumps(data, indent=4, separators=(",", ": "), ensure_ascii=False))
    #
    # PEsort = sorted(PERatio, key=lambda PE: PE[1])
    #
    # for symbol in PEsort:
    #     print(symbol[0] + ": {}\n".format(symbol[1]))