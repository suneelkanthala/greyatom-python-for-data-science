# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#print(type(data))
#print(data)
census = np.concatenate((data, new_record),axis = 0)
#print(data.shape)
#print(census.shape)
age = np.array([census[:,0]])
#print(age)
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

#print(max_age,min_age,round(age_mean,2),round(age_std,2))

race_0, race_1, race_2, race_3, race_4 = census[census[:,2] == 0], census[census[:,2] == 1], census[census[:,2] == 2], census[census[:,2] == 3], census[census[:,2] == 4]

len_0, len_1, len_2, len_3, len_4 = len(race_0), len(race_1), len(race_2), len(race_3), len(race_4)
minimum = min(len_0,len_1,len_2,len_3,len_4)
if len_0 == minimum:
    minority_race = 0
elif len_1 == minimum:
    minority_race = 1
elif len_2 == minimum:
    minority_race = 2
elif len_3 == minimum:
    minority_race = 3
elif len_4 == minimum:
    minority_race = 4

print(minority_race)

senior_citizens = census[census[:,0] > 60]
working_hours_sum = np.sum(senior_citizens[:,6])
avg_working_hours = working_hours_sum / len(senior_citizens)
print(working_hours_sum)
print(round(avg_working_hours,2))

high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(round(avg_pay_high,2),round(avg_pay_low,2))




