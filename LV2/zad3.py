

'''Na temelju primjera 2.5. učitajte sliku 'tiger.png'. Manipulacijom odgovarajuće numpy matrice pokušajte:
a) posvijetliti sliku (povećati brightness),
b) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
c) zrcaliti sliku,
d) smanjiti rezoluciju slike x puta (npr. 10 puta),
e) prikazati samo drugu četvrtinu slike po širini, a prikazati sliku cijelu po visini; ostali dijelovi slike trebaju biti
crni.'''


import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("C:\\Users\\Matija ciki\\Desktop\\LV2\\tiger.png")
img = img[:,:,0].copy()
img_array=[]
print(img.shape)
print(img.dtype)
plt.figure()


plt.imshow(np.rot90(img), cmap="gray")
plt.show()
plt.imshow(np.fliplr(img), cmap="gray")
plt.show()


img_array=img+0.6
img_array[img_array>1]=1

plt.figure(1)
plt.title("a) brightness")
plt.imshow(img_array,cmap='gray')

img3 = img[::5,::5] #smanjena kvaliteta

plt.figure(4)
plt.title("d) smanjena kvaliteta slike")
plt.imshow(img3,cmap='gray')
redovi = img.shape[0] #broj redova
stupci = img.shape[1] #broj stupaca
dg = stupci//4
gg = stupci//2

pr_img = img.copy()
for i in range(redovi):
    for j in range(stupci):
        if (j < dg or j > gg): 
            pr_img[i][j] = 0



plt.figure(5)
plt.title("e) stupci")
plt.imshow(pr_img, cmap='gray')
plt.show()
