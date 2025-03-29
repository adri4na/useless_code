import math
''' 
useless script to calculate Kab = ab^K
is it useful? no
does it matter? tampoco
try different bases

found 1 and 25
then (after 2 minutes) I had real things to do 
'''

#set_in= range(1000000,10000000)
set_in= range(1,100000)
z_s = range(150)
k = False
for z in z_s :
    for i in set_in:
        sq = i**z
        if i%10 != 0 and i != 1 :
            kdec = math.ceil(math.log10(i)) #to get nearest 10 power
        else :
            kdec = math.ceil(math.log10(i)) + 1
        sq_wanted = z*(10**kdec) + i
        if sq_wanted == sq :
            print(f'FOUND! {i}^{z} = {sq}')
            k=True

if not k :
    print("Found none")
