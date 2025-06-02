def respond(user_query):
    if "sustainable" in user_query.lower():
        recommend = max(
            crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It’s eco-friendly (Score: {crypto_db[recommend]['sustainability_score']}/10)."
    elif "trend" in user_query.lower():
        recommend = [coin for coin in crypto_db if crypto_db[coin]
                     ["price_trend"] == "rising"]
        return f"Trending coins: {', '.join(recommend)} 📈"
    else:
        return "Ask me about sustainability or price trends!"
