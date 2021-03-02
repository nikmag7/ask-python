lek=raw_input("eisagete arxeio")
def bathos(leksiko):
    if isinstance(leksiko, dict):
        return 1 + (max(map(bathos, leksiko.values())) if leksiko else 0)
    return 0
leks={'a':1,'b':{'c':{'d':{}}}}
print (bathos(lek))
