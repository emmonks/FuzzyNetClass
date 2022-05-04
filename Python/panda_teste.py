import pandas as pd
df = pd.read_csv (r'/home/core/Capturas/Capturas_Doutorado/videos_iscx2016q.csv')
#print (df)
# block 2 - group by
#groupby_sum1 = df.groupby(['Label']).sum() 
#groupby_count1 = df.groupby(['Label']).count()

#print ('Sum of values, grouped by the Label: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Label: ' + str(groupby_count1))

# block 1 - simple stats
mean1_t = df['Flow IAT Mean'].mean()
mean1 = mean1_t / 1000

#sum1 = df['Salary'].sum()
max1 = df['Flow IAT Mean'].max()
min1 = df['Flow IAT Mean'].min()
#count1 = df['Salary'].count()
median1 = df['Flow IAT Mean'].median() 
std1 = df['Flow IAT Mean'].std() 
var1 = df['Flow IAT Mean'].var() 
dur1_t = df['Flow Duration'].mean()
dur1 = dur1_t / 1000 / 1000

# print block 1
print ('Mean Flow IAT Mean: ' + str(mean1))
#print ('Sum of salaries: ' + str(sum1))
print ('Max Flow IAT Mean: ' + str(max1))
print ('Min Flow IAT Mean: ' + str(min1))
#print ('Count of salaries: ' + str(count1))
print ('Median Flow IAT Mean: ' + str(median1))
print ('Std of Flow IAT Means: ' + str(std1))
print ('Var of Flow IAT Means: ' + str(var1))
print ('Duration: ' + str(dur1))
