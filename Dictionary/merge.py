
dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50, 6:60} 

dict = {}
dict.update(dic1)
dict.update(dic2)
dict.update(dic3)

new_dict = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", dict)
