from pyit2fls import zero_mf, singleton_mf, const_mf, tri_mf, ltri_mf, rtri_mf, trapezoid_mf, gaussian_mf
import matplotlib.pyplot as plt
from numpy import linspace

# domain1 = linspace(4., 10, 1000)
# domain2 = linspace(0., 5, 1000)
# domain3 = linspace(8., 14, 1000)
# # mySet = T1FS(domain, trapezoid_mf, [4, 6, 8, 10, 1.0])
# # mySet.plot()


# trapezoid = trapezoid_mf(domain1, [4, 6, 8, 10, 1.0])
# ltri = tri_mf(domain2, [0, 4, 5, 1.0])
# rtri = tri_mf(domain3, [8, 10, 14, 1.0 ])

# plt.figure()
# plt.plot(domain2, ltri, label="Ringan")
# plt.plot(domain1, trapezoid, label="Sedang")
# plt.plot(domain3, rtri, label="Berat")
# plt.grid(True)
# plt.legend()
# plt.xlabel("Berat Pakaian")
# plt.ylabel("Membership function")
# plt.savefig('fungsi_keanggotaan_berat_pakaian.png')
# plt.show()

domain1 = linspace(30., 100, 1000)
domain2 = linspace(0., 50, 1000)
domain3 = linspace(70., 120, 1000)
# mySet = T1FS(domain, trapezoid_mf, [4, 6, 8, 10, 1.0])
# mySet.plot()


trapezoid1 = trapezoid_mf(domain1, [30, 50, 70, 100, 1.0])
trapezoid2 = trapezoid_mf(domain2, [-10, -5, 30, 50, 1.0])
trapezoid3 = trapezoid_mf(domain3, [70, 100, 150, 1500, 1.0])
# ltri = tri_mf(domain2, [0, 30, 50, 1.0])
# rtri = tri_mf(domain3, [70, 100, 120, 1.0 ])

plt.figure()
plt.plot(domain2, trapezoid2, label="Cepat")
plt.plot(domain1, trapezoid1, label="Sedang")
plt.plot(domain3, trapezoid3, label="Lama")
plt.grid(True)
plt.legend()
plt.xlabel("Durasi Cuci")
plt.ylabel("Membership function")
# plt.savefig('fungsi_keanggotaan_durasi_cuci.png')
plt.show()