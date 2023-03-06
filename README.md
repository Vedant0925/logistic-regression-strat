# logistic-regression-strat
***NOT VERY FINANCIALLY INCLINED***

Basic rundown-

1. import required modules from modules.py

2. histdata.py to choose targeted stocks. Manually create a new folder on your system before running this part.
//Make sure that you are not targeting more than 2,000 tickers, because the Yfinance API has a 2,000 API calls per hour limit.//

3. histdata2.py to obtain the historical price data of each stock in our tickers list by making independent calls to Yahoo Finance. After receiving the        data, the program will save each company’s information in a new CSV file that will be located in the folder you created beforehand.

4. techind.py to import the technical indicators. These 32+ technical indicators will act as predictor variables for the dependent variable. Made use of      three variables for time frames. The three variables are 5, 30, and 60 day observations of the closing prices of each stock (1 if it increased and 0 if    it did not).

5. logreg.py to clean the data (remove infinite and null values), run the logistic regression model, and interpret the results. I have performed a random      split of the data but it would be recommended to go 80/20 instead.
