#!/usr/bin/env python
# coding: utf-8

# In[ ]:


soal 1

x = input("Masukkan Kata pertama : ")
y = input("Masukkan kata kedua  : ")

pecah1= []
for i in x:
    pecah1 = pecah1+[i]

counter = 0
for cek in y:
    if cek in pecah1:
        counter = counter + 1
    else:
        pass

if counter == len(x):
    print('Kata yang anda masukkan Anagram')
else:
    print("Kata yang anda masukkan bukan Anagram")


# In[ ]:


soal 2

def jumlah(kalimat, kata):
    kalimat = kalimat.lower()
    a = kalimat.count(kata)
    return a

kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang ingin dicari frekunsinya: ")
print(jumlah(kalimat, kata))


# In[ ]:


soal 3

kalimat = input("Masukkan kalimat:  ")
hapus = " ".join(kalimat.split())
print(hapus)


# In[ ]:


soal 4

def kalimat (a):
    step = a.split()
    pen = ""
    pan = ""
    for i in range(len(step)):
        if i == 0:
            pen = step[0]
            pan = step[0]
        else:
            if len(pan) < len(step[i]):
                pan = step[i]
            if len(pen) > len(step[i]):
                pen = step[i]

    print(pan)
    print(pen)

x = input("Masukkan kalimat: ")
kalimat(x)

