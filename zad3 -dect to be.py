#dekadni u  binarni

def binconv(broj):

    if broj > 1:
         ren= broj%2
         broj= broj//2
         return binconv(broj) + str(ren)


    else:
        return str(broj)


print(binconv(1205682))
