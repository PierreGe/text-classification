

nbrTest = [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

classificationPercent = [75, 71, 58, 47, 44, 41, 40, 39, 39, 38 , 37]


import matplotlib.pyplot as plt
plt.plot(nbrTest, classificationPercent, 'ro')

plt.xlabel('Number of attributes')
plt.ylabel('Correctly classified')
plt.title('Chi-squarred attributes selection')
plt.axis([0, 1000, 0, 100])
plt.savefig("part2.png")