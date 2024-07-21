#DESCRIPTION: Library to quickly convert dates to and from strings using the yyyy-mm-dd format.
#AUTHOR:      Zachary Collier
#DATE:        June 15th, 2024

import datetime

def strToDateConv(dateToConv):
    dateReturn = datetime.datetime.strptime(dateToConv, '%Y-%m-%d')
    return dateReturn

def dateToStrConv(dateToConv):
    dateReturn = datetime.datetime.strftime(dateToConv, '%Y-%m-%d')
    return dateReturn
