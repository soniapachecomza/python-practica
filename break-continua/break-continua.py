c = 0

while c < 10:
    c += 1
    print (c)

    if c == 5:
        #print ("Termina el bucle")
        print ("Salta la siguiente iteración")
        #break
        continue
else:
    print ("Fin de while")