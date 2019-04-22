import formula
import data
import worktools
from matplotlib import pyplot as plt
size_of_men = int(data.get_size())

rating = []
zn = 0
zn = int(zn)
for i in range(size_of_men):
    zn =zn+1
    temp = formula.get_rating(data.get_size(),level = data.get_level(zn),size_of_relationships=data.get_relationships(zn))
    rating.append(temp)
    
print(rating)
name = []
zn = 0
for i in range(size_of_men):
    zn =zn+1
    temp = data.get_data_id(zn)[1]
    name.append(temp)
print(name)

plt.bar(name,rating)
plt.show()
data_work = []
med = worktools.median(rating)
data_work.append(med)
print('median ',med)
mod = worktools.mode(rating)
data_work.append(mod[0])
print('mode' ,mod[0])
disp = worktools.variance(rating)
data_work.append(disp)
print('disp' ,disp)

print(data_work)
names =['медиана','мода','дисперсия']
plt.bar(names,data_work)
plt.show()