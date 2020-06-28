import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum() # 累加数据

# DataFrame
data=pd.DataFrame(np.random.randn(1000,4),
                index=np.arange(1000),
                columns=list("ABCD")) # columns=["A","B","C","D"]
print(data.head(5))
data=data.cumsum()
print(data.head(5)) # head()默認前5
data.head(5).plot()
plt.show()

# plot methods: "bar", "hist", "box", "kde", "area", "scatter", "hexbin", "pie"...... 
ax=data.plot.scatter(x="A",y="B",color="DarkBlue",label="Class 1")
data.plot.scatter(x="A",y="C",color="DarkGreen",label="Class 2",ax=ax) # 将之画在上一个ax上面, ax=
plt.show()



