'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #print(word)
    #Variable to hold amount of instances
    count = 0
    #Base Case when the word has less than two letters remaining
    if len(word) < 2:
        return 0
    #If the first two letters of the word have 'th' and return a count
    #take off the first letter and run the function again
    elif word[0:2] == 'th':
        count += 1
        return count_th(word[1:]) + count
    #If it does not just take off the first letter and run it again
    else:
        return count_th(word[1:])


print(count_th('thisshouldhave1'))
print(count_th('shouldhavenone'))
print(count_th('thththththththTH'))