#importing matplotlib
import matplotlib.pyplot as plt
#making birth rate
birth=[1,4,12,9,10,15,16]
days=[" Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
plt.bar(birth,days,color='pink',width=1)
plt.show()