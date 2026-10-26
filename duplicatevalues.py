# Duplicate Values

def containsDuplicate(self, nums):
    if(len(set(nums)) == len(nums):
       return False
    else:
       return True
                      
                      

# use a python set
# sets in python cannot have duplicate values,
# so taking a set of the original list then
# comparing it to the original list can tell us
# if there are any duplicates