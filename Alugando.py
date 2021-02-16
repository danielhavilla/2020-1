q_dias = int(input())
q_total = int(input())

if q_total <= 100:
    
    print("{:.2f}".format(q_dias*90))

else:
    q_total = q_total - (q_dias*100)
    
    print("{:.2f}".format((q_dias*90)+(q_total*12)))