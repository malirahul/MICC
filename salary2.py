"""clean the 
           messy salary 
                        from list
                    """
                    
salaries=['$876,001','$543,903','$2453,896']
for s in salaries:
    messy=(int(''.join(s[1:].split(','))))
    print(messy)
