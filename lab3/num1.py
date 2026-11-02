lst = [1,2,3,4,5,6]
tuple = (1,2,3,4,5,6)
print(f"0 List: {lst}, {type(lst)}, {id(lst)}")
print(f"0 Tuple: {tuple}, {type(tuple)}, {id(tuple)}")

lst[-1] = 23
print(f"1 List: {lst}, {type(lst)}, {id(lst)}")


tuple2 = (11,2,3,4,5,6)
print(f"1 Tuple: {tuple is tuple2}, Tuple: {type(tuple)}, {id(tuple)}, Tuple2 {type(tuple2)}, {id(tuple2)}")