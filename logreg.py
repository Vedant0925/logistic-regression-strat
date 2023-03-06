Hold_Results = []
list_files2 = (glob.glob("<Your Path>\\Bayesian_Logistic_Regression\\Stocks_Sub\\*.csv")) # Creates a list of all csv filenames in the stocks folder
for interval2 in list_files2:
    Stock_Name = ((os.path.basename(interval2)).split(".csv")[0])
    data = pd.read_csv(interval2,index_col=0)
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.fillna(0)
    dependents = [data["Five_Day_Observation_Outcome"].to_list(), data["Thirty_Day_Observation_Outcome"].to_list(), data["Sixty_Day_Observation_Outcome"].to_list()]
    data = data.drop(['Five_Day_Observation_Outcome', 'Thirty_Day_Observation_Outcome', 'Sixty_Day_Observation_Outcome', 'Date', 'Open', 'High', 'Low', 'Close'], axis = 1)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)  # Standardize our data set
    Hold_Results_Section = []
    p = 0
    for dep in dependents:
        x_train, x_test, y_train, y_test =\
        train_test_split(data, dep, test_size=0.2, random_state=0)
        model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr',random_state=0)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)  # To get the predicted values
        conf = confusion_matrix(y_test, y_pred)
        if p == 0:
            Hold_Results.append([Stock_Name, "Five_Day_Observation_Outcome", model.score(x_train, y_train),model.score(x_test, y_test),conf[0,0],conf[0,1],conf[1,0],conf[1,1]])
        if p == 1:
            Hold_Results.append([Stock_Name, "Thirty_Day_Observation_Outcome", model.score(x_train, y_train),model.score(x_test, y_test),conf[0,0],conf[0,1],conf[1,0],conf[1,1]])
        if p == 2:
            Hold_Results.append([Stock_Name, "Sixty_Day_Observation_Outcome", model.score(x_train, y_train),model.score(x_test, y_test),conf[0,0],conf[0,1],conf[1,0],conf[1,1]])
        p+=1
    print("Model complete for " + Stock_Name)
df = pd.DataFrame(Hold_Results, columns=['Stock', 'Observation Period', 'Model Accuracy on Training Data', 'Model Accuracy on Test Data', 'True Positives','False Positives',
'False Negative','True Negative'])
df.to_csv("<Your Path>\\Bayesian_Logistic_Regression\\Model_Outcome.csv", index = False)
