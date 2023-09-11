import numpy as np
import matplotlib.pyplot as plt

veri = {"a" : np.arange(50),
        "c" : np.random.randint(0,50,50),
        "d" : np.random.randn(50)}
veri["b"] = veri["a"] + (10 * np.random.randn(50))
veri["d"] = np.abs(veri['d']) * 100

plt.scatter("a","b", c="c", s="d", data = veri)
plt.xlabel("a sütunundaki veriler")
plt.ylabel("b sütunundaki veriler")
plt.show()