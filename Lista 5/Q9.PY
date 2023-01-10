var = 'Arcoverde'
inv = len(var)
for x in range((len(var) +1) * 2):
    if x < len(var):
        print(var[:x])
    elif x > len (var):
        print(var[:inv])    
        inv -= 1 