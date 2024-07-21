#DESCRIPTION: Program for One Stop Insurance Company to enter and calculate new insurance policy information for customers.
#             This program allows you to write previous claims into a .dat file. Useful for something like a database!
#AUTHOR:      Zachary Collier
#DATE:        July 16th 2024

#Import required libraries

import datetime
import time
import DateConvLib
import DollarConvLib
import ProgressBars

#Define constants (from default values file)

f = open('ConstAlt.dat', 'r')
POLICY_NO = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COVERAGE = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PROCESS_FEE = float(f.readline())
f.close()

VALID_PROVINCES = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
VALID_PAY_METHODS = ["F", "M", "D"]

#Display Constants (debug only)

'''print(POLICY_NO)
print(BASIC_PREMIUM)
print(ADD_CAR_DISCOUNT)
print(EXTRA_LIABILITY_COVERAGE)
print(GLASS_COVERAGE)
print(LOANER_COVERAGE)
print(HST_RATE)
print(MONTHLY_PROCESS_FEE)'''

#Define functions

def ErrorMessage(Message):#Prints an error message with the desired message
    print("--!--")
    print(f"ERR: {Message}")
    print("--!--")

def ListValidation(Variable, List):#Checks if a variable is part of a list
    validation = False
    for i in range(len(List)):
        if Variable == List[i]:
            validation = True
    
    return validation

def PostalValidation(Post):#Checks if a postal code is in a valid format
    postNums = Post[1] + Post[3] + Post[5]
    postNums = postNums.isdigit()
    postLets = Post[0] + Post[2] + Post[4]
    postLets = postLets.isalpha()
    postValid = False

    if postNums == False:
        ErrorMessage("Please ensure numbers are the second, fourth, and sixth characters.")
    elif postLets == False:
        ErrorMessage("Please ensure letters are the first, third, and fifth characters.")
    else:
        postValid = True
    
    return postValid

#Main Program

while True:
    #Gather user inputs

    custFirst = input("Enter the customer's first name: ").title()
    custLast = input("Enter the customer's last name: ").title()
    custAddress = input("Enter the customer's address: ")
    custCity = input("Enter the customer's city: ").title()

    while True:
        custProv = input("Enter the customer's province (in the abbreviated, 2-letter format): ").upper()
        if len(custProv) != 2:
            ErrorMessage("Please use the abbreviated province name (i.e. 'NL' for Newfoundland & Labrador)")
        else:
            custProvVal = ListValidation(custProv, VALID_PROVINCES)
            if custProvVal:
                break
            else:
                ErrorMessage("Invalid province abbreviation.")
    
    while True:
        custPostal = input("Enter customer's postal code (LNLNLN): ").upper()
        if len(custPostal) != 6:
            ErrorMessage("Please ensure 6 characters are used for the postal code.")
        else:
            custPostalVal = PostalValidation(custPostal)
            if custPostalVal:
                break
    
    while True:
        custPhone = str(input("Enter customer's phone number (10-digit number): "))
        if len(custPhone) != 10 or custPhone.isdigit() == False:
            ErrorMessage("Please ensure 10 numbers are used for the phone number.")
        else:
            custPhoneDsp = f"({custPhone[:3]}) {custPhone[3:6]}-{custPhone[6:]}"
            break
    
    while True:
        try:
            numCarsDsp = input("Enter the number of cars the customer has insured: ")
            numCars = int(numCarsDsp)
        except:
            ErrorMessage("Please ensure only numbers are used.")
        else:
            break
    
    while True:
        custExtraLiability = input("Extra liability up to $1,000,000? (Y for Yes, N for No): ").upper()
        if (custExtraLiability == "Y" or custExtraLiability == "N") and len(custExtraLiability) == 1:
            break
        else:
            ErrorMessage("Please enter only either Y or N.")
    
    while True:
        custGlassCover = input("Optional Glass coverage? (Y for Yes, N for No): ").upper()
        if (custGlassCover == "Y" or custGlassCover == "N") and len(custGlassCover) == 1:
            break
        else:
            ErrorMessage("Please enter only either Y or N.")

    while True:
        custLoaner = input("Optional Loaner Car? (Y for Yes, N for No): ").upper()
        if (custLoaner == "Y" or custLoaner == "N") and len(custLoaner) == 1:
            break
        else:
            ErrorMessage("Please enter only either Y or N.")

    while True:
        custPayMethod = input("What is the customer's payment method (F for Full, M for Monthly, D for Down Pay): ")
        if len(custPayMethod) != 1:
            ErrorMessage("Please enter only either F, M, or D.")
        else:
            custPayMethodVal = ListValidation(custPayMethod, VALID_PAY_METHODS)
            if custPayMethodVal:
                break
            else:
                ErrorMessage("Invalid pay method.")
    
    downPayAmount = 0
    if custPayMethod == "D":
        while True:
            try:
                downPayAmountDsp = input("Down Payment selected, please enter the down payment amount: ")
                downPayAmount = float(downPayAmountDsp)
            except:
                ErrorMessage("Please enter only numbers.")
            else:
                downPayAmountDsp = DollarConvLib.dollarConv(downPaymentAmount)
                break
    
    claimNoList = []
    claimDateList = []
    claimAmountList = []
    claimAmountListRaw = []

    while True:
        while True:
            try:
                claimNoDsp = input("Enter the customer's previous claim's number: ")
                claimNo = int(claimNoDsp)
            except:
                ErrorMessage("Please enter only numbers.")
            else:
                claimNoList.append(claimNoDsp)
                break
        
        while True:
            try:
                claimDateDsp = input("Enter the claim date (YYYY-MM-DD): ")
                claimDate = DateConvLib.strToDateConv(claimDateDsp)
            except:
                ErrorMessage("Invalid date entered.")
            else:
                claimDateList.append(claimDateDsp)
                break

        while True:
            try:
                claimAmount = input("Enter the claim amount: ")
                claimAmount = float(claimAmount)
            except:
                ErrorMessage("Please enter only numbers.")
            else:
                claimAmountListRaw.append(claimAmount)
                claimAmountList.append(DollarConvLib.dollarConv(claimAmount))
                break
        
        while True:
            claimEnterContinue = input("Add more claims? (Y for Yes, N for No): ").upper()
            if (claimEnterContinue == "Y" or claimEnterContinue == "N") and len(claimEnterContinue) == 1:
                break
            else:
                ErrorMessage("Please enter only either Y or N.")
        
        if claimEnterContinue == "N":
            break

    #Perform Calculations

    if custPayMethod == 'F':
        custPayMethod = 'Full'
    elif custPayMethod == 'M':
        custPayMethod = 'Monthly'
    else:
        custPayMethod = 'Down Payment'

    insurancePremiums = BASIC_PREMIUM + (numCars - 1) * BASIC_PREMIUM * (1 - ADD_CAR_DISCOUNT)

    extraLiabilityCost = 0
    if custExtraLiability == "Y":
        extraLiabilityCost = EXTRA_LIABILITY_COVERAGE * numCars
    
    glassCost = 0
    if custGlassCover == "Y":
        glassCost = GLASS_COVERAGE * numCars
    
    loanerCost = 0
    if custLoaner == "Y":
        loanerCost = LOANER_COVERAGE * numCars

    totalExtraCost = extraLiabilityCost + glassCost + loanerCost
    totalInsurancePremium = totalExtraCost + insurancePremiums
    taxes = totalInsurancePremium * HST_RATE

    totalCost = totalInsurancePremium + taxes

    if custPayMethod != 'Full':
        monthlyPayment = (MONTHLY_PROCESS_FEE + totalCost - downPayAmount) / 8
        monthlyPaymentDsp = DollarConvLib.dollarConv(monthlyPayment)
    else:
        monthlyPaymentDsp = 'N/A'
    
    if downPayAmount == 0:
        downPayAmountDsp = 'N/A'

    today = datetime.datetime.now()
    todayStr = DateConvLib.dateToStrConv(today)
    todayMonth = todayStr[5:7]
    todayYear = todayStr[:4]
    if todayMonth == "12":
        firstPayYear = int(todayYear) + 1
        firstPayMonth = 1
    else:
        firstPayYear = int(todayYear)
        firstPayMonth = int(todayMonth) + 1
    
    firstPayDate = datetime.datetime(firstPayYear, firstPayMonth, 1)
    firstPayDateDsp = DateConvLib.dateToStrConv(firstPayDate)

    #Display outputs

    insurancePremiumsDsp = DollarConvLib.dollarConv(insurancePremiums)
    extraLiabilityCostDsp = DollarConvLib.dollarConv(extraLiabilityCost)
    glassCostDsp = DollarConvLib.dollarConv(glassCost)
    loanerCostDsp = DollarConvLib.dollarConv(loanerCost)

    totalExtraCostDsp = DollarConvLib.dollarConv(totalExtraCost)
    totalInsurancePremiumDsp = DollarConvLib.dollarConv(totalInsurancePremium)
    taxesDsp = DollarConvLib.dollarConv(taxes)
    totalCostDsp = DollarConvLib.dollarConv(totalCost)

    print(f'''
    ------------------------------------------------
                   ONE STOP INSURANCE
                        RECIEPT
    ------------------------------------------------

      Customer:
      {(custFirst + '' + custLast):<25s}    Policy #: {str(POLICY_NO):<5s}
      Home Address:                Phone #:
      {custAddress:<25s}    {custPhoneDsp:<14s}
      {custCity:<13s}, {custProv:<2s}, {custPostal:<6s}

    ------------------------------------------------

      Options:

        Extra liability up to $1,000,000?: {custExtraLiability}
        Glass coverage?                    {custGlassCover}
        Loaner car?                        {custLoaner}

    ------------------------------------------------

      Payment Method: {custPayMethod:<12s}
      Number of vehicles: {numCarsDsp:<3s}

             ITEM         |         AMOUNT
    ----------------------|------------------------
      Insurance Premiums  |  {insurancePremiumsDsp:>20s}
    ----------------------|------------------------
      Extra Liability     |  {extraLiabilityCostDsp:>20s}
      Glass Coverage      |  {glassCostDsp:>20s}
      Loaner Car          |  {loanerCostDsp:>20s}
      Total Extra Cost    |  {totalExtraCostDsp:>20s}
    ----------------------|------------------------
      Total Premiums      |  {totalInsurancePremiumDsp:>20s}
      HST                 |  {taxesDsp:>20s}
      Total Cost          |  {totalCostDsp:>20s}
    ----------------------|------------------------
      Down Payment        |  {downPayAmountDsp:>20s}
      Monthly Payments    |  {monthlyPaymentDsp:>20s}
    -----------------------------------------------
      Invoice Date:       {todayStr:<10s}
      First Payment Date: {firstPayDateDsp:<10s}

      CLAIM # | CLAIM DATE | AMOUNT
    ----------|------------|-------------''')
    for i in range(len(claimNoList)):
        print(f"      {claimNoList[i]:^6s}  | {claimDateList[i]:^10s} | {claimAmountList[i]:>10s}")

    #Write values to files

    f = open('PolicyInfoAlt.dat', 'a') #Contains all policy holder info
    f.write('{}, '.format(POLICY_NO)) #PK
    f.write('{}, '.format(custFirst))
    f.write('{}, '.format(custLast))
    f.write('{}, '.format(custAddress))
    f.write('{}, '.format(custCity))
    f.write('{}, '.format(custProv))
    f.write('{}, '.format(custPostal))
    f.write('{}, '.format(custPhoneDsp))
    f.write('{}, '.format(numCarsDsp))
    f.write('{}, '.format(custExtraLiability))
    f.write('{}, '.format(custGlassCover))
    f.write('{}, '.format(custLoaner))
    f.write('{}, '.format(custPayMethod))
    f.write('{}, '.format(downPayAmountDsp))
    f.write('{}\n'.format(totalInsurancePremiumDsp))
    f.close()

    f = open('PastClaimsAlt.dat', 'a') #Contains all past claims of a designated policy holder
    for i in range(len(claimNoList)):
        f.write('{}, '.format(claimNoList[i])) #PK
        f.write('{}, '.format(POLICY_NO)) #FK
        f.write('{}, '.format(claimDateList[i]))
        f.write('{}\n'.format(claimAmountListRaw[i]))
    f.close()
    #More organized for a theoretical database's use

    POLICY_NO += 1 #Increase policy number

    #Progress Bar

    print()
    TotalIterations = 30
    Message = "Saving Data ..."
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  # Simulate some work
        ProgressBars.ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
    print()
    print()

    #Continue Program Validation

    while True:
        continueProgram = input("Continue running the program? (Y for Yes, N for No): ").upper()
        if (continueProgram == "Y" or continueProgram == "N") and len(continueProgram) == 1:
            break
        else:
            ErrorMessage("Please enter only either Y or N.")
    
    if continueProgram == "N":
        print("Thank you for using this program. Have a great day!")
        break

#Housekeeping

f = open('ConstAlt.dat', 'w')
f.write('{}\n'.format(POLICY_NO))
f.write('{}\n'.format(BASIC_PREMIUM))
f.write('{}\n'.format(ADD_CAR_DISCOUNT))
f.write('{}\n'.format(EXTRA_LIABILITY_COVERAGE))
f.write('{}\n'.format(GLASS_COVERAGE))
f.write('{}\n'.format(LOANER_COVERAGE))
f.write('{}\n'.format(HST_RATE))
f.write('{}\n'.format(MONTHLY_PROCESS_FEE))
f.close()