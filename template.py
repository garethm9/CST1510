"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :    Cyber 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("enter a name or hostname or ip")
first = float(input("enter first value"))
second = float(input("enter second value"))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]

difference = second - first
percentage = first/second * 100

# =================================================================== OUTPUT
# 3. Print the report.

print("=" * 34)
print(label)
print(first)
print(second)
print("=" * 34)
value = difference + percentage
print(f"{value:>10.2f}")
print(f"{difference:>+10.2f}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
