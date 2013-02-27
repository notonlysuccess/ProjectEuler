from math import *
from operator import *

#year and day
def leap(y):
	return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

def nextDay(y , m , d):
	d += 1
	if (m in (4,6,9,11) and d == 31) or (m in (1,3,5,7,8,10,12) and d == 32) or (m == 2 and ((leap(y) and d == 30) or (not leap(y) and d == 29))):
		d = 1
		m += 1
	if m == 13:
		m = 1
		y += 1
	return y , m , d

#gcd and lcm
def gcd(a , b):
	if b == 0:return a
	return gcd(b , a % b)

def lcm(a , b):
	return a * b / gcd(a , b)

def reduceF(a , b):
	g = gcd(a,b)
	return a/g , b/g

#number base tran
def dec2bin(s):
	num = int(s)
	b = []
	while num:
		num , rem = divmod(num , 2)
		b += [rem]
	return ''.join([str(x) for x in b[::-1]])

#perm
def perm(s):
	n = len(s)
	for i in range(len(s)):
		v = s[i:i+1]
		if n == 1:
			yield v
		else:
			rest = s[:i]+s[i+1:]
			for result in perm(rest):
				yield v + result
#prime
def getIsPrime(n):
	isPrime = [False] * 2 + [True] * (n - 2)
	for i in range(n):
		if isPrime[i]:
			isPrime[i*i::i] = [False] * len(isPrime[i*i::i])
	return isPrime

def same(a):
	for x in a:
		if x != a[0]: return False
	return True
	
def getPrime(n):
	isPrime = getIsPrime(n)
	return [x for x in range(len(isPrime)) if isPrime[x]]

def isPrime(n):
	for i in xrange(2 , int(n**0.5 + 1)):
		if n % i == 0:
			return False
	return True
		
def fuckPrime(n , prime):
	if n == 1:
		return [(1,1)]
	ret = []
	b = int(n**0.5 + 1)
	for p in prime:
		if p > b: break
		if n % p == 0:
			n /= p
			cnt = 1
			while n % p == 0:
				n /= p
				cnt += 1
			ret.append((p , cnt))
	if n != 1:
		ret.append((n , 1))
	return ret

def getFactors(n):
	b = int(n**0.5 + 1)
	result = 1
	for i in xrange(1 , b):
		if n % i == 0:
			j = n / i
			yield i
			if i != j:
				yield j


def powmod(a,b,mod):
	ret = 1
	while b:
		if b & 1:
			ret *= a
			if ret >= mod:
				ret %= mod
		a *= a
		if a >= mod:
			a %= mod
		b >>= 1
	return ret
