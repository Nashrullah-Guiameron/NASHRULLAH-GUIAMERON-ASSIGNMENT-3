import numpy as np

# Save to a text file (csv format)
# EXAMPLE 3

#1 save and wirte text file
Example3 = np.arange(20)
np.savetxt('Example3.csv', Example3, delimiter=',')


#2 Load data from text file
Example3 = np.loadtxt('Example3.csv', delimiter=',')
print(Example3)


