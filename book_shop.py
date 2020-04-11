#Book Shop

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ] 
invoice_totals = list(map(lambda x:(x[0],x[2] * x[3]), orders))
print(invoice_totals)

"""The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR."""
    
    
min_value = 100
total = list(map(lambda x:x 
                 if x[1] >= min_value
                 else (x[0], x[1] + 10), 
			              map(lambda x:(x[0],x[2] * x[3]), orders)))

print(total)
