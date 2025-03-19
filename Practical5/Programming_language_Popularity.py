#make a dictionary of the language using 
language_use = {
    "JavaScript":62.3,
    "HTML":52.9,
    "Python":51,
    "SQL":51,
    "TypeScript":38.5
    }

#print the dictionary above
print(language_use)

#draw the plot describing the data
#import the package numpy to calculate and matplotlib to draw graph
import numpy as np
import matplotlib.pyplot as plt

#set variables of x and y axis
languages = list(language_use.keys())
percentages = list(language_use.values())

#set the width of the bar 
width = 0.5

#draw the graph
barplot = plt.bar(languages, percentages, width)
plt.ylabel('Persentages')
plt.title('Programming Language Popularity')
plt.xticks(languages)
plt.yticks(np.arange(0, 80, 10))

#show the graph
plt.show()

#responde to the input language types and eliminate the upper or lower form of the input
lower_languages = [lang.lower() for lang in languages]
required_language = "Python"
if required_language.lower() in lower_languages:
    print(f"The percentage of {required_language} is {language_use[required_language]}%.")
else:
    print(f"{required_language} is not included in the list.")