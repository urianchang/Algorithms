import calendar
import datetime
from typing import Dict, List, NamedTuple, Optional


class Subscription(NamedTuple):
    id: int
    customer_id: float
    monthly_price_in_dollars: int


class User(NamedTuple):
    id: int
    name: str
    customer_id: int
    
    # when this user started
    activated_on: datetime.date
      
    # last day to bill for user
    # should bill up to and including this date
    deactivated_on: datetime.date
      
      
def bill_for(month: str, active_subscription: Subscription, users: List[User]) -> float:
    # Early exit in case customer does not have an active subscription
    if not active_subscription:
      return 0
    
    month = datetime.datetime.strptime(month, "%Y-%m").date()
    first_of_month = first_day_of_month(month)
    last_of_month = last_day_of_month(month) + datetime.timedelta(days=1)  # We want to include the last day
    
    total_days: int = (last_of_month - first_of_month).days
    daily_rate: float = active_subscription["monthly_price_in_dollars"] / total_days
    
    customer_id: int = active_subscription['customer_id']
    total_bill: float = 0
    
    # Find number of days that each user is active in the billing month
    # TODO: Clean up by putting this logic in a separate function
    for user in users:
      if user['customer_id'] == customer_id:
        activated = user['activated_on']
        
        # User isn't active yet
        if activated > last_of_month:
          continue
        
        if activated < first_of_month:
          start = first_of_month
        else:
          start = activated
        
        deactivated = user['deactivated_on']
        if deactivated is None:
          end = last_of_month
        elif deactivated < last_of_month:
          end = deactivated
        else:
          end = last_of_month
        
        active_days = (end - start).days
        total_bill += active_days * daily_rate
    
    return round(total_bill, 2)    

  
####################
# Helper functions #
####################

def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:
    
    >>> first_day_of_month(datetime.date(2019, 2, 7))  # Feb 7
    datetime.date(2019, 2, 1)                          # Feb 1
    
    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)

def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:
    
    >>> last_day_of_month(datetime.date(2019, 2, 7))  # Feb  7
    datetime.date(2019, 2, 28)                        # Feb 28
    
    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return datetime.date(date.year, date.month, last_day)

def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:
    
    >>> next_day(datetime.date(2019, 2, 7))   # Feb 7
    datetime.date(2019, 2, 8)                 # Feb 8

    >>> next_day(datetime.date(2019, 2, 28))  # Feb 28
    datetime.date(2019, 3, 1)                 # Mar  1
    
    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)


