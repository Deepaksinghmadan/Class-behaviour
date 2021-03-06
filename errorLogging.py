sring = open('errors.log').read()
print(sring.count('DEBUG'))
print(sring.count('INFO'))
print(sring.count('WARNING'))
print(sring.count('ERROR'))
print(sring.count('CRITICAL'))

import matplotlib.pyplot as plt
plt.bar([1],[sring.count('DEBUG')],label="DEBUG")
plt.bar([2],[sring.count('INFO')],label="DEBUG")
plt.bar([3],[sring.count('WARNING')],label="DEBUG")
plt.bar([4],[sring.count('ERROR')],label="DEBUG")
plt.bar([5],[sring.count('CRITICAL')],label="DEBUG",color="black")
plt.legend()
plt.show()
