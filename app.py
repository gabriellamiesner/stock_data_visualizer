
from datetime import date, datetime
import time
import pygal

#API KEY 
API_KEY = "AH4E9KX41PXBFQQI"

#Symbol Selection 
SYMBOL = input("Enter the stock symbol you would like to use: ")

def select_time_series():
    #user selection (dont know how to link user slection with a variable)
    print("Select the time series of the chart that you want generate")
    print("----------------------------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")

    #dictionary of all the choices
    times = {
        "Intraday" : "TIME_SERIES_INTRADAY",
        "Daily" : "TIME_SERIES_DAILY",
        "Weekly" : "TIME_SERIES_WEEKLY",
        "Monthly" : "TIME_SERIES_MONTHLY",
    }

    # List of choices (so choice is accessible via index)
    time_choices = ["TIME_SERIES_INTRADAY", "TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", "TIME_SERIES_MONTHLY"]

    time_selection = ""
    time_series_selection = ""

    # Input validation
    while True:
        #user input selection
        time_series_selection = input("Enter the time series option you would like to select: ")
        try:
            #new variable is assigned based on selection
            #time_selection = times_[timeSeriesSelection]
            time_selection = time_choices[int(time_series_selection) - 1]
            if (int(time_series_selection) <= 0):
                print('Invalid input! Time series selection must be a number 1-4.')
                continue
            else:
                break
        except ValueError:
            print('Invalid input! Time series selection must be a number 1-4.')
        except IndexError:
            print('Invalid input! Time series selection must be a number 1-4.')


    #startDate = input("Enter the start date: (YYYY-MM-DD) ")
    #endDate = input("Enter the end date: (YYYY-MM-DD) ")
    #startDate = startDate.split("-")
    #print(datetime(int(startDate[0]), int(startDate[1]), int(startDate[2])))

    ogURL = "https://www.alphavantage.co/query?function={}&symbol={}&apikey={}".format(time_selection, SYMBOL, API_KEY)

    if time_series_selection == "1":    # "1" is the equivalent option for Intraday
        print("Time intervals")
        print("---------------")
        print("1 - 1 minute")
        print("5 - 5 minutes")
        print("15 - 15 minutes")
        print("30 - 30 minutes")
        print("60 - 60 minutes")

        #dictionary of all choices
        intervals = {
            "1" : "1min",
            "5" : "5min",
            "15" : "15min",
            "30" : "30min",
            "60" : "60min",
        }

        interval_selection = ""
        while True:
            interval_series_selection = input("Enter a time interval that you would like to select:")
            try:
                interval_selection = intervals[interval_series_selection]
                break
            except:
                print('Invalid input! Interval selection must be a number 1, 5, 15, 30, or 60.')

        ogURL = "https://www.alphavantage.co/query?function={}&symbol={}&interval={}&apikey={}".format(time_selection, SYMBOL, interval_selection, API_KEY)

        # Test print statement
        #print(ogURL)

        return ogURL

def select_chart_type():
    # Note: when calling this method, it must be set to a variable as it returns an
    # instance of the graph selected (Line or Bar)

    # Printed menu
    print('Chart Types')
    print('\n---------------')
    print('1. Bar')
    print('2. Line')

    # Input validation
    chart_selection = 0
    while True:
        try:
            chart_selection = int(input('Select a chart type: '))
            if chart_selection < 1 or chart_selection > 2:
                print('Invalid input! Chart selection must be one of the provided options.')
                continue
            else:
                break
        except ValueError:
            print('Invalid input! Chart selection must be a number 1 or 2.')

    # Return an instance of the chart selected by the user
    if chart_selection == 1:
        return pygal.Line()
    elif chart_selection == 2:
        return pygal.Bar()

def main():
    ogURL = select_time_series()
    chart = select_chart_type()

    # Test print statements
    print(ogURL)
    print(chart)

main()