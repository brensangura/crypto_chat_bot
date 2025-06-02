if "green" in user_query:
    recommend = [coin for coin in crypto_db if crypto_db[coin]
                 ["sustainability_score"] >= 7]
