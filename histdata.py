# List of the stocks we are interested in analyzing. At the time of writing this, it narrows the list of stocks down to 44.
# If you have a list of your own you would like to use just create a new list instead of using this, for example: tickers = ["FB", "AMZN", ...] 
tickers = gt.get_tickers_filtered(mktcap_min=150000, mktcap_max=10000000)

# Check that the amount of tickers isn't more than 2000
print("The amount of stocks chosen to observe: " + str(len(tickers)))

# These two lines remove the Stocks folder and then recreate it in order to remove old stocks. Make sure you have created a Stocks Folder the first time you run this.
shutil.rmtree("<Your Path>\\Bayesian_Logistic_Regression\\Stocks\\")
os.mkdir("<Your Path>\\Bayesian_Logistic_Regression\\Stocks\\")
