import numpy as np

# list1 = [[1,2] , [3,4], [5,6]]
# ar = np.array(list1)
# print(list1)
# print(ar)
# ar = np.ones((2,3 , 5))
# print(ar.shape)
# ar = np.random.randint(5 , 15 , (2,5))
# ar = np.ones(12)
# ar = ar.reshape(3,4)
# print(ar)

# list1 = [1,2,3,1]
# list2 = [4,5,6,5]
# arr1 = np.array(list1)
# arr2 = np.array(list2)
# result = [x * y for x ,y in zip(list1 , list2)]
# print(result)
# print(list1 * list2)
# print(arr1 * arr2)

# ar = np.ones((3,5))
# print(ar[0:2 , 1:4])
import pandas as pd
# df = pd.DataFrame(columns=["names" , "age" , "gender" , "grade"],
#                   data=[
#                       ["yahya" , "25" , "male" , "95"],
#                       ["ali" , "26" , "male" , "85"],
#                       ["rani" , "24" , "male" ,"90"]
#                   ]
#                   )
# print(df.info())
# df.to_csv("data.csv" , index=False)
# df.to_excel("data1.XLSX")
# data  = {
#     "names" : ["yahya" , "ali" , "rani"],
#     "age" : [25 , "26" , 24],
#     "gender" : ["male" , "male" , "male"],
#     "grade" : [95 , 85 , 90]
# }
# df2 = pd.DataFrame(data)
# print(df2.info())
data = pd.read_csv("data.csv")
# print(data.duplicated().sum())
# print(data.loc[1,"grade"])
# print(data.iloc[1,3])
data = data.drop(0)
data["age"] = data["age"].apply(lambda x :x +3)
print(data)
# print(data.groupby('names')['grade'].mean())
