import matplotlib.pyplot as plt
isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma"]
degerler = [5,25,50,100]
plt.figure(figsize=(9,3))

plt.subplot(131)
plt.bar(isimler,degerler)

plt.subplot(132)
plt.scatter(isimler,degerler)

plt.subplot(133)
plt.plot(isimler,degerler)

plt.suptitle("Birçok farklı grafik")
plt.show()