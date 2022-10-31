import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def predict(deaths, timestamp):
    url = r"E:\IIT\4th Year\FYP\Dataset\Bitcoin Historical Data.csv"
    df = pd.read_csv(url)

    from sklearn import preprocessing

    df['Date'] = preprocessing.LabelEncoder().fit_transform(df['Date'].values)
    df['Deaths'] = preprocessing.LabelEncoder().fit_transform(df['Deaths'].values)
    df['Pandemic disaster'] = preprocessing.LabelEncoder().fit_transform(df['Pandemic disaster'].values)
    required_features = ['Deaths', 'Timestamp']
    output_label = 'Price'
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(df[required_features],
    df[output_label],
    test_size = 0.3,
    random_state=0)

    from sklearn.linear_model import LinearRegression
    linear = LinearRegression()
    linear.fit(X_train, Y_train)

    from sklearn.ensemble import AdaBoostRegressor
    adb = AdaBoostRegressor()
    adb.fit(X_train, Y_train)

    from sklearn.ensemble import RandomForestRegressor
    classifier = RandomForestRegressor()
    classifier.fit(X_train, Y_train)

    from sklearn.ensemble import GradientBoostingRegressor
    gbr = GradientBoostingRegressor(random_state=0)
    gbr.fit(X_train, Y_train)

    from sklearn.ensemble import VotingRegressor
    voting = VotingRegressor([("linear", linear), ("classifier",classifier), ("adb", adb),("gbr", gbr)])
    voting.fit(X_train, Y_train)

    X_new = pd.DataFrame({'Deaths': [deaths],'Timestamp': [timestamp]})
    predict_value = voting.predict(X_new)
    predict_price = str(predict_value)
    return predict_price