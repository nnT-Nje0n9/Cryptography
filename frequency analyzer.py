#Frequency Analyzer
import numpy as np
import matplotlib.pyplot as plt


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dic = {}
cipher = input("Input The Cipher to analyze : ")

for i in alphabet:
    dic[i] = cipher.count(i)
    print(i, " : ", cipher.count(i))

for i in list(dic.keys()): #delete the element has 0 value
    if dic[i] == 0:
        del dic[i]

dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=False)) #sort

x = list(dic.keys())
y = list(dic.values())

plt.barh(x,y)
plt.show()
