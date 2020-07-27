# RSI_Notifier
A programme which ask for stock tickers you are interested in. Returning a 'BUY'/'HOLD'/'SELL' rating depending on the RSI (Relative Strength Index) of the stock. The RSI is a useful tool to measure whether something is being 'over-bought' or 'over-sold'.

Essentially what the code does is pull data from the API 'Alpha Vantage' -- The data it pulls is the RSI for individual stocks. Once this data is pulled the programme creates a CSV with just the latest RSI figure ('.tail(1)).
The programme then simply runs a basic if/elif/else block determining whether the stock is a BUY/HOLD/SELL depending on the RSI number extracted.
