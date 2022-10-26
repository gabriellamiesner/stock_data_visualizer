import pygal

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
            print('Invalid input! Chart selection must be an integer.')

    # Return an instance of the chart selected by the user
    if chart_selection == 1:
        return pygal.Line()
    elif chart_selection == 2:
        return pygal.Bar()