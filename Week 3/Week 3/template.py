"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1.

# your function(s) go here
def status_of(percent):
    """returns the status of each percent"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """calculates difference and percent then returns both values"""
    difference = limit - value 
    percent = difference/value *100
    return difference
    return percent

def print_report(label, value, limit, difference, percent, status):
    """prints a report of all the parameters"""
    print(label)
    print(value)
    print(limit)
    print(difference)
    print(percent)
    print(status)


# ==================================================================== INPUT
# 2.

label = input("enter a name or hostname or ip")
value = float(input("enter a value"))
limit = float(input("enter a limit"))

# ================================================================== PROCESS
# 3. 

difference = limit - value
percent = difference/value * 100
status = status_of(percent)
check(value, limit)

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here
print("=" * 34)
print("label", label)
print("value", value)
print("limit", limit)
print("=" * 34)
diffper = difference + percent
print(f"{diffper:.2f}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
