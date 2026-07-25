import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

# x = np.random.randint(10 , 100 , 5)
# x1 = np.random.randint(10 , 100 , 5)
# y = np.random.randint(1,10 , 5)
# y1 = np.random.randint(1,10 , 5)
# print(x)
# print(y)
# plt.figure(figsize=(8,5))
# plt.plot(x , y , marker= "o" , color="red" , linestyle="--" , label="red line")
# plt.plot(x1 , y1 , marker= "o" , color="blue" , label="blue line")
# plt.title("is Raqndom numbers")
# plt.xlabel("x random values")
# plt.ylabel("y random values")
# plt.legend("lower left")
# plt.grid(axis="y")
# plt.show()
data = {
    "Months" : ["Nov" , "Dec" , "Jan" , "Feb" , "Mach"],
    "toyta" : [ 2500 , 2400 , 3600 , 4920 , 4360],
    "BMW" : [3400 , 6500 ,7800 ,9200 , 4500],
    "mareceds" : [6500 , 5320 , 4561 , 7842 , 6532]
}

df = pd.DataFrame(data)
width = 0.25
x = np.arange(len(df["Months"]))
print(df)
plt.figure(figsize=(7,5))
plt.bar(x , df["toyta"] , width , color="#cf2065" , label="Toyta scels" )
plt.bar(x - width , df["BMW"] , width , color="#1a7749" , label="BMW scels" )
plt.bar(x + width , df["mareceds"] , width , color="#050706" , label="Mareceds scels" )
plt.xlabel("Months")
plt.ylabel("Scalles")
plt.xticks( x , df["Months"])
plt.legend()
plt.show()
sizes = [30, 25, 20, 25]
labels = ['IT', 'HR', 'Sales', 'Finance']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Employee Distribution by Department')
plt.show()