# These two lines remove the Stocks folder and then recreate it in order to remove old stocks. Make sure you have created a Stocks Folder the first time you run this.
shutil.rmtree("<Your Path>\\Bayesian_Logistic_Regression\\Stocks_Sub\\")
os.mkdir("<Your Path>\\Bayesian_Logistic_Regression\\Stocks_Sub\\")

# Get the Y values
list_files = (glob.glob("<Your Path>\\Bayesian_Logistic_Regression\\Stocks\\*.csv")) # Creates a list of all csv filenames in the stocks folder
for interval in list_files:
    Stock_Name = ((os.path.basename(interval)).split(".csv")[0])
    data = pd.read_csv(interval)
    dropna(data)
    data = add_all_ta_features(data, open="Open", high="High", low="Low", close="Close", volume="Volume")
    data = data.iloc[100:]
    close_prices = data['Close'].tolist()
    Five_Day_Obs = []
    thirty_Day_Obs = []
    sixty_Day_Obs = []
    x = 0
    while x < (len(data)):
        if x < (len(data)-5):
            if ((close_prices[x+1] + close_prices[x+2] + close_prices[x+3] + close_prices[x+4] + close_prices[x+5])/5) > close_prices[x]:
                Five_Day_Obs.append(1)
            else:
                Five_Day_Obs.append(0)
        else:
            Five_Day_Obs.append(0)
        x+=1
    y = 0
    while y < (len(data)):
        if y < (len(data)-30):
            ThirtyDayCalc = 0
            y2 = 0
            while y2 < 30:
                ThirtyDayCalc = ThirtyDayCalc + close_prices[y+y2]
                y2 += 1
            if (ThirtyDayCalc/30) > close_prices[y]:
                thirty_Day_Obs.append(1)
            else:
                thirty_Day_Obs.append(0)
        else:
            thirty_Day_Obs.append(0)
        y+=1
    z = 0
    while z < (len(data)):
        if z < (len(data)-60):
            SixtyDayCalc = 0
            z2 = 0
            while z2 < 60:
                SixtyDayCalc = SixtyDayCalc + close_prices[z+z2]
                z2 += 1
            if (SixtyDayCalc/60) > close_prices[z]:
                sixty_Day_Obs.append(1)
            else:
                sixty_Day_Obs.append(0)
        else:
            sixty_Day_Obs.append(0)
        z+=1
    data['Five_Day_Observation_Outcome'] = Five_Day_Obs
    data['Thirty_Day_Observation_Outcome'] = thirty_Day_Obs
    data['Sixty_Day_Observation_Outcome'] = sixty_Day_Obs
    data.to_csv("<Your Path>\\Bayesian_Logistic_Regression\\Stocks_Sub\\"+Stock_Name+".csv")
    print("Data for " + Stock_Name + " has been substantiated with technical features.")
