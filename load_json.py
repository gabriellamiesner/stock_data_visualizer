import requests
import json
from datetime import datetime

# Variables below are TEST values only
beginning_date = datetime(2020, 10, 1)
end_date = datetime(2022, 10, 1)

# The URL below is a test value to be replaced by the actual URL query
request_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=demo'
response = requests.get(request_url).text
response_data = json.loads(response)

#print(response_data)

data = []
# !! Note: Each time series has a different name for the value used below; it will need to change dynamically
for entry in response_data['Weekly Adjusted Time Series']:
    date_format = '%Y-%m-%d'
    raw_datetime = datetime.strptime(entry, date_format)
    if raw_datetime >= beginning_date and raw_datetime <= end_date:
        data.append({'Date':entry, 'Data':response_data['Weekly Adjusted Time Series'][entry]})


# Sources:
# - https://www.geeksforgeeks.org/converting-string-yyyy-mm-dd-into-datetime-in-python/
# - https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0
# - 