 # import necessary libraries 

import pandas as pd 

import matplotlib.pyplot as plt 

 
 

# get input data 

df = pd.read_csv('CSV file name') 

 
 

df.plot(x='x axix name ', y='y axix name ') 

plt.title('title of graph') 

plt.xlabel("x axix lable") 

plt.ylabel("y axix lable") 

plt.show() 


# co-realtion between two graph

 

import pandas as pd  

# Read the first CSV file into a pandas dataframe 

df1 = pd.read_csv('csv file 1 name') 

# Read the second CSV file into a pandas dataframe 

df2 = pd.read_csv('csv file 2 name') 

 # Select the same two columns from each dataframe 

#col1_df1 = df1['Years'] 

col2_df1 = df1['data of csv file 1'] 

#col1_df2 = df2['Years'] 

col2_df2 = df2['data of csv file 2 '] 

# Calculate correlation coefficient between the two columns from each dataframe 

corr_coef = col2_df1.corr(col2_df2)  

# Print the result 

print(f"Correlation coefficient between column1 and column2: {corr_coef}") 

 