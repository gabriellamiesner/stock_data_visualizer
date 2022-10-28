import datetime
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
while True: 
    try: 
        startDate = input("Enter the start date: (YYYY-MM-DD) ")
        startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
        break;
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")

while True: 
    try: 
        endDate = input("Enter the end date: (YYYY-MM-DD) ")
        endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
        if endDate > startDate:
            break;
        else: 
            print("Incorrect data format, End date should occur after the start date.")
    except ValueError: 
        print("Incorrect data format, should be YYYY-MM-DD.")





# print(datetime(int(startDate[0]), int(startDate[1]), int(startDate[2])))



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