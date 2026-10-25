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

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    def __init__(self, label, value, limit):
        """initialising the classes attributess"""
        self.label = label
        self.value = value
        self.limit = limit
        self.over_limit = 0

    def status(self):
        """returns the status of value as a percentage of limit"""
        percent = self.value/self.limit * 100
        if percent >= self.limit:
            self.over_limit += 1
            return "OVER LIMIT"
        elif percent >=90:
            return "WARNING"
        else:
            return "OK"

    


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

record1 = Record("R-001", 50, 100)
record2 = Record("R-002", 70, 100)
print(record1.status())
print(record2.status())

with open("records.txt", "w")as f:
    f.write("R-001", 50, 100\n)
    f.write("R-002", 70, 100\n)

def load_records(path):
    recordlist = []
    try:

        with open(path, "r") as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                value = float(value)
                limit = float(limit)
                recordlist.append(label, value, limit)

    except FileNotFoundError:
        print("file not found")
    return recordlist

load_records("records.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

overlimit_count = 0
for record in recordlist:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f" label: {record.label}")
    print(f" value: {record.value:.2f}")
    print(f" limit: {record.limit:.2f}")
    print(f" status: {record.status()}")
    print("=" * 34)
    if record.status() == "OVER LIMIT":
       overlimit_count += 1

    print("the over limit count is", overlimit_count)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring