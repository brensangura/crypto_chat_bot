if "profit" in user_query:
    recommend = [coin for coin in crypto_db if crypto_db[coin]["price_trend"]
                 == "rising" and crypto_db[coin]["market_cap"] == "high"]
