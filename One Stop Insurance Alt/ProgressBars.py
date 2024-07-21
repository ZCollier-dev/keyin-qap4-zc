#DESCRIPTION: Library to add a progress bar to a program.
#AUTHOR:      Compiled by Zachary Collier
# From the url: https://handhikayp.medium.com/creating-terminal-progress-bar-using-python-without-external-library-b51dd907129c
#DATE:        July 11th 2024

import sys
import datetime
import time

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

'''To initialize the progress bar:
print()
TotalIterations = 30
Message = "Saving Data ..."
for i in range(TotalIterations + 1):
    time.sleep(0.1)  # Simulate some work
    ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
print()
print()
'''

def BlinkingMessage(blinkNo):
    for _ in range(blinkNo):  # Change to control no. of 'blinks'
        print(Message, end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)