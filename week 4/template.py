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
def check_record(value, limit):
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



# ====================================================================== STORE
# 2. 

records = ["label", "value", "limit"]
def load_records(path):
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            value = float(value)
            limit = float(limit)
            return records


        

# =============================================================== PROCESS + OUTPUT
# 3. 

for records in records:
    check_record(records["value"], records["limit"])
    print_report(records["lables"], records["value"],records["limit"])

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
