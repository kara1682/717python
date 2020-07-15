#print('%10s%10s%10s' % ('name','age','address'))
#print('%-10s%-10s%-10s' % ('name','age','address'))
#print("\n")
#print('{:10}{:10}{:10}'.format('name','age','address'))
#print('{:>10}{:>10}{:>10}'.format('name','age','address'))
#print('{:<10}{:<10}{:<10}'.format('name','age','address'))
#print('{:^10}{:^10}{:^10}'.format('name','age','address'))
#print('{:-^10}{:-^10}{:-^10}'.format('name','age','address'))

# 화폐단위 1000단위 컴머
print('{:,}{:,}'.format(10000,10000))

# IP address 192.168.108.11
a1=(192)
a2=(168)
a3=(108)
a4=(11)
print(a1,a2,a3,a4,sep=".")

print('binary print {:b}'.format(192))
print('binary print {:b}.{:b}.{:b}.{:b}'.format(192,168,108,11))

print('{0} {1} {2} {3} {4} {5}'.format('The','famine','was','severe','is','Samaria'))
print('{4} {5} {2} {3} {0} {1}'.format('The','famine','was','severe','is','Samaria'))

