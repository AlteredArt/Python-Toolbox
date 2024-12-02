def sizely(size):
    counter = 0 
    finalString = []

    while size >= counter:
        finalString.append(1)
        
        while size >= counter:
            finalString.append(0)

        counter += 1
    
    print(finalString)

sizely(9)