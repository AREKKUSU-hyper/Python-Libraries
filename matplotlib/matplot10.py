import matplotlib.pyplot as plt
plt.figure()

# plt.subplot(2,2,1)
# plt.plot([0,1],[0,1])
# plt.subplot(2,2,2)
# plt.plot([0,1],[0,2])
# plt.subplot(2,2,3)    # plt.subplot(2,2,3)可以简写成plt.subplot(223)
# plt.plot([0,1],[0,3])
# plt.subplot(224)      
# plt.plot([0,1],[0,4])

plt.subplot(3,1,1)
plt.plot([0,1],[0,1])
plt.subplot(334)
plt.plot([0,1],[0,2])
plt.subplot(335)
plt.plot([0,1],[0,3])
plt.subplot(336)
plt.plot([0,1],[0,4])
plt.subplot(313)
plt.plot([0,1],[0,10])



plt.show()