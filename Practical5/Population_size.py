#store the population sizes for the UK and Zhejiang-neiphbouring provines
uk_contries = [57.11, 3.13, 1.91, 5.45]
zj_neibour_provines = [65.77, 41.88, 45.28, 61.27, 85.15]

#sort the contries of the uk and provines of china
sorted_uk = sorted(uk_contries)
sorted_zj = sorted(zj_neibour_provines)

#show the sorted population
print("Sorted population of UK countries:", sorted_uk,
      "\nSorted population of some Chinese provines:", sorted_zj)

#import the package of drawing
import matplotlib.pyplot as plt

#set the lable names of the axis
labels_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland']
explode = (0, 0, 0, 0.2)

#plot the graph by using the pie chart
plt.pie(uk_contries, 
        explode = explode, 
        labels = labels_uk, 
        autopct = '%1.2f%%', 
        shadow = False, 
        startangle = 90)

#make sure the pie is a circle
plt.axis('equal')
plt.show()

labels_ch = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
explode = (0, 0, 0, 0.2, 0)
plt.pie(zj_neibour_provines, 
        explode = explode, 
        labels = labels_ch, 
        autopct = '%1.1f%%', 
        shadow = False, 
        startangle = 90)

#make sure the pie is a circle
plt.axis("equal")
plt.show()