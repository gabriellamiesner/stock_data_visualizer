
#API KEY 
API_KEY = "AH4E9KX41PXBFQQI"

#Symbol Selection 
SYMBOL = input("Enter the stock symbol you would like to use: ")

#user selection (dont know how to link user slection with a variable)
print("Select the time series of the chart that you want generate")
print("----------------------------------------------------------")
print("1. Intraday")
print("2. Daily")
print("3. Weekly")
print("4. Monthly")

#user input selection
timeSeriesSelection = input("Enter the time series option you would like to select: ")

#dictornay of all the choices
times = {
    "Intraday" : "TIME_SERIES_INTRADAY",
    "Daily" : "TIME_SERIES_DAILY",
    "Weekly" : "TIME_SERIES_WEEKLY",
    "Montly" : "TIME_SERIES_MONTHLY",
}

#new variable is assgned based on selection
timeSelection = times[timeSeriesSelection]

ogURL = "https://www.alphavantage.co/query?function={}&symbol={}&apikey={}".format(timeSelection,SYMBOL,API_KEY)

if timeSeriesSelection == "Intraday":

    intervalSeriesSelection = input("Enter a time interval that you would like to select:")


    #dictionary of all choices
    intervals = {
        "1 minute" : "1min",
        "5 minutes" : "5min",
        "15 minutes" : "15min",
        "30 minutes" : "30min",
        "60 minutes" : "60min",

    }
    intervalSelection = intervals[intervalSeriesSelection]

    ogURL = "https://www.alphavantage.co/query?function={}&symbol={}&interval={}&apikey={}".format(timeSelection,SYMBOL,intervalSelection, API_KEY)






print(ogURL)