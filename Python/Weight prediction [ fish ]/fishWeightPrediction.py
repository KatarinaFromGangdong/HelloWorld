import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df=pd.read_csv("I:\My Drive\HelloWorld\Python\Weight prediction [ fish ]\Fish.csv")
# df=pd.read_csv("I:\My Drive\HelloWorld\Python\Weight prediction [ fish ]\SampleFishData.csv")
head = df.head()
info = df.info()
is_null = df.isnull().sum()
species = df.Species.value_counts()
describe = df.describe()
shape = df.shape
print("\nhead\n",head,"\ninformation\n", info,"\n\nis null\n", is_null,"\n\nspecies\n", species,"\n\ndescribe\n", describe,"\n\nshape\n", shape)

# diff plot representation
# sns.countplot(data=df,x='Species')
# sns.pairplot(data= df, x_vars = ['Length1','Length2','Length3','Height','Width'], y_vars ='Weight',hue='Species')
# graphical representation, mamimili ka sa dalawa ☝🏻
# sns.heatmap(df.corr(),annot=True)
# sns.boxplot(df['Weight'])
# plt.show()

# weight outliers
fish_weight = df['Weight']
Q3 = fish_weight.quantile(0.75)
Q1 = fish_weight.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 -(1.5*IQR)
upper_limit = Q3 +(1.5*IQR)
weight_outliers = fish_weight[(fish_weight <lower_limit) | (fish_weight >upper_limit)]
print("\nweight outliers\n", weight_outliers)

# length_1 outliers
fish_Length1 = df['Length1']
Q3 = fish_Length1.quantile(0.75)
Q1 = fish_Length1.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 -(1.5*IQR)
upper_limit = Q3 +(1.5*IQR)
length1_outliers = fish_Length1[(fish_Length1 <lower_limit) | (fish_Length1 >upper_limit)]
print("\n\nlength_1 outliers\n",length1_outliers)

# length_2 outliers
fish_Length2 = df['Length2']
Q3 = fish_Length2.quantile(0.75)
Q1 = fish_Length2.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 -(1.5*IQR)
upper_limit = Q3 +(1.5*IQR)
length2_outliers = fish_Length2[(fish_Length2 <lower_limit) | (fish_Length2 >upper_limit)]
length2_outliers
print("\n\nlength_2 outliers\n",length1_outliers)

# length_3 outliers
fish_Length3 = df['Length3']
Q3 = fish_Length3.quantile(0.75)
Q1 = fish_Length3.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 -(1.5*IQR)
upper_limit = Q3 +(1.5*IQR)
length3_outliers = fish_Length3[(fish_Length3 <lower_limit) | (fish_Length3 >upper_limit)]
print("\n\nlength_3 outliers\n", length3_outliers)

df1=df.drop([142,143,144])
print("\n\ndf1\n",df1.shape)

final_df=df1.drop(['Species'],axis=1)
print("\n\nfinal df\n",final_df.tail())

# sklearn
X=final_df.drop(['Weight'],axis=1)
y=final_df['Weight']
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=100)
model=linear_model.LinearRegression()
print("\n\nalgorithm model: ",model.fit(xtrain,ytrain))

# prediction x test
pred=model.predict(xtest)
c = [i for i in range(1,48,1)]
plt.plot(c, ytest,color = 'Blue')
plt.plot(c, pred,color = 'red')
plt.title('Test(Blue) vs pred(Red)')
print("\n\nTEST\n",ytest,"\n\nPREDICTION\n", pred)
plt.show()