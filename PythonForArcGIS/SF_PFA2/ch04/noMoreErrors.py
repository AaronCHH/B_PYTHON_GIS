# Name: NoMoreErrors.py

dataName = 'Lucca.gdb'
county = 'Dyer'
id = 20

# 1. Print the name of the script.
print 'NoMoreErrors.py

# 2. Print the last chararcter in dataName
print dataName[11]

# 3. Use a string method to change the first letter
#    of dataName to M ('Mucca.gdb' not 'Lucca.gdb')
#    and print the results
dataName[0] = 'M'
print dataName

# 4. Concatenate county and id and print the results
fullName = county + id
print fullName

# 5. Print the county in all caps.
allCaps = county.upper(0)
print allCaps

# 6. Print the feedback message or the last line of the traceback resulting
# from each erroroneous line in #1-5 before each was repaired. #1 and 2 are
# done for you.
print '#1. FEEDBACK BAR: Failed to check - syntax error - EOL while scanning string literal'
print '#2. TRACEBACK: IndexError: string index out of range'
print "#3. TRACEBACK: ???"
print "#4. TRACEBACK: ???"
print '#5. TRACEBACK: ???'
