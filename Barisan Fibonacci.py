nterms = int(input())
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print()
elif nterms == 1:
   print(nterms)
   print(n1)
else:
   print()
   while count < nterms:
       print("Bilangan Fibonacci ke-",count,": ",n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1