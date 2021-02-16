entrada1 = int(input())
entrada2 = int(input())
entrada3 = int(input())

if entrada1 < entrada2 and entrada1 < entrada3:
        print(entrada1)
        if entrada2 < entrada3:
            print(entrada2)
            print(entrada3)
        else:
            print(entrada3)
            print(entrada2)
        
if entrada2 < entrada1 and entrada2 < entrada3:  
        print(entrada2)
        if entrada1 < entrada3:
            print(entrada1)
            print(entrada3)
        else:
            print(entrada3)
            print(entrada1)

if entrada3 < entrada1 and entrada3 < entrada2: 
        print(entrada3)
        if entrada1 < entrada2:
            print(entrada1)
            print(entrada2)
        else:
            print(entrada2)
            print(entrada1)
            
if entrada1 == entrada2 and entrada1 < entrada3:
            print(entrada1)
            print(entrada1)
            print(entrada3)

if entrada2 == entrada3 and entrada2 < entrada1:
            print(entrada2)
            print(entrada2)
            print(entrada1)
            
if entrada3 == entrada1 and entrada3 < entrada2:
            print(entrada3)
            print(entrada3)
            print(entrada2)
            
if entrada1 == entrada2 and entrada1 == entrada3:
            print(entrada1)
            print(entrada1)
            print(entrada1)


            


            

           


        
        
        

    
        


