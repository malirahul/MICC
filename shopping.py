#Shopping List

shopping_list=[]
print("Enter the item : ")
print("Enter 'DONE' to stop adding items")
while(True):
    new_item=input('=>')
    if new_item=='DONE':
        break
    
    shopping_list.append(new_item)
    print("Shopping List : ")
    for item in shopping_list:
        print(item)
        