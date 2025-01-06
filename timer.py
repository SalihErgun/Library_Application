from datetime import datetime, timedelta

# Function to get the current time and the time two weeks later
def loan_dates():
    # Get the current time
    borrow_date = datetime.now()
    
    # Calculate the time two weeks later
    return_date = borrow_date + timedelta(weeks=2)
    
    # Return both dates as strings in the desired format
    return borrow_date.strftime('%Y-%m-%d %H:%M:%S'), return_date.strftime('%Y-%m-%d %H:%M:%S')
