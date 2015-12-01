

nbrTest = [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

classificationPercent = [75, 71, 58, 47, 44, 41, 40, 39, 39, 38 , 37]


import matplotlib.pyplot as plt
plt.plot(nbrTest, classificationPercent, 'ro')

plt.xlabel('Number of attributes')
plt.ylabel('Correctly classified (%)')
plt.title('Test numero 1')
plt.axis([0, 1000, 0, 100])
plt.savefig("part2.png")
plt.close()

nbrTest = [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

classificationPercent = [72.5, 75.3, 77.1, 78.2, 77.8, 78.6, 79.1, 79.4, 79.1, 79.1 , 79.5]

plt.plot(nbrTest, classificationPercent, 'ro')

plt.xlabel('Number of attributes')
plt.ylabel('Correctly classified (%)')
plt.title('Test numero 2')
plt.axis([0, 1000, 0, 100])
plt.savefig("part2b.png")
plt.close