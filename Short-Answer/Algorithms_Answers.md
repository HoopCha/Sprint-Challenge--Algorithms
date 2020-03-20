#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
If we plug a couple different n options is and see how many times it runs:
1 means it runs once
2 means it runs twice
3 means it runs three times...
This pattern continues onward leading me to believe it is O(n)

b)
line 1: O(1)
line 2: O(n)
    line 3: O(1)
    line 4: O(n)
        line 5: O(1)
        line 6: O(1)
line 7: O(1)

Gets condesed too:
line 2: O(1 + (n * (2 * n)) + 1)     

Which if I have done my algebra correctly, leads me to think that this is O(n^2)


c)
This one seems pretyt simple again, for each bunny, it will run once and then subtract a bunny, leading me to beleive it is O(n), its essentially just a for loop

## Exercise II

I would do a bianary search, so I would start by going half way up the building and dropping the egg, then depending on the results, cut that in half again and again until the last remaining floor is the one where i can drop it from without the egg breaking. 

The runtim ecomplexity for this would O(log N)
