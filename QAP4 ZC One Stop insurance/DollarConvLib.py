#DESCRIPTION: Library to quickly convert dollar values to strings in the format $#,###.##
#AUTHOR:      Zachary Collier
#DATE:        June 15th, 2024

def dollarConv(dollarValue):
    dollarValueStr = "${:,.2f}".format(dollarValue)
    return dollarValueStr
