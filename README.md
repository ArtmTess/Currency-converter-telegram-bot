# Currency-converter-telegram-bot

The telegram bot is called @QA_currency_bot, search for it in a telegram app.

This bot converts a given amount of a given currency to another given currency. 

Bot's commands:

/start
a welcome message and instructions for using the bot.

/values
list of supported currencies

Commands should always start with the '/' symbol.


The currency rates are dynamic and taken from global cryptocurrency market data provider CryptoCompare. More about CryptoCompare here: https://www.cryptocompare.com/about-us/

For currency value used the API get method with three arguments: 
- "base": the currency you want to know,
- "quote": the name of the currency in which the price is to be found,
- "amount": the amount of the transferred currency,
and returns the required amount in the currency.

The user should send a request for the bot by following this pattern: <Currency1 Currency2 100> by using space to separate.

When a user makes an incorrect input APIException is called with a user-friendly error explanation. 

Files structure:
app.py - telegram bot,
config.py is storage for the token and currencies list,
exceptions.py - possible users error with friendly explanations.



