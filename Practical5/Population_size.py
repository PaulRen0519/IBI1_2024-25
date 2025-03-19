# store the population sizes for the UK and Zhejiang-neighbouring provinces
uk_countries = [57.11, 3.13, 1.91, 5.45]
zj_neighbour_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]

# sort the countries of the uk and provinces of china
sorted_uk = sorted(uk_countries)
sorted_zj = sorted(zj_neighbour_provinces)

# show the sorted population
print("Sorted population of UK countries:", sorted_uk,
      "\nSorted population of some Chinese provinces:", sorted_zj)

# import the package of drawing
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# set the label names of the axis
labels_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland']
explode = (0, 0, 0, 0.2)

# use subplot to add two graph to one fiture
fig, (ax1, ax2) = plt.subplots(1, 2)

# draw the first chart
ax1.pie(sorted_uk, explode=explode, labels=labels_uk, autopct='%1.1f%%')
ax1.set_title('UK Population')

# define the chinese label
labels_ch = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']

# draw the second fiture
ax2.pie(sorted_zj, labels=labels_ch, autopct='%1.1f%%')
ax2.set_title('Chinese Provinces Population')

plt.tight_layout()
plt.show()