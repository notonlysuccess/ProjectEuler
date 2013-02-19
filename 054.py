def SameValue(cards):
	for c in cards:
		if c[0] != cards[0][0]:
			return False
	return True

def HighCard(cards):
	ret = [1]
	for c in cards:
		ret.append(c[0])
	return ret

def OnePair(cards):
	if (SameValue(cards[:2])):
		return [2 , cards[0][0] , cards[2][0] , cards[3][0] , cards[4][0]]
	if (SameValue(cards[1:3])):
		return [2 , cards[1][0] , cards[0][0] , cards[3][0] , cards[4][0]]
	if (SameValue(cards[2:4])):
		return [2 , cards[2][0] , cards[0][0] , cards[1][0] , cards[4][0]]
	if (SameValue(cards[3:])):
		return [2 , cards[3][0] , cards[0][0] , cards[1][0] , cards[2][0]]
	else:
		return False
	
def TwoPair(cards):
	if SameValue(cards[:2]) and SameValue(cards[2:4]):
		return [3 , cards[0][0] , cards[2][0] , cards[4][0]]
	elif SameValue(cards[:2]) and SameValue(cards[3:]):
		return [3 , cards[0][0] , cards[3][0] , cards[2][0]]
	elif SameValue(cards[1:3]) and SameValue(cards[3:]):
		return [3 , cards[1][0] , cards[3][0] , cards[0][0]]
	else:
		return False

def ThreeOfAKind(cards):
	for i in xrange(3):
		if SameValue(cards[i:i+3]):
			return [4 , cards[i][0]]
	return False

def Straight(cards):
	for i in xrange(1 , 5):
		if cards[i][0] != cards[i-1][0] - 1:
			return False
	return [5 , cards[0][0] ]

def Flush(cards):
	ret = [6]
	for c in cards:
		if c[1] != cards[0][1]:
			return False
		else:
			ret.append(c[0])
	return ret

def FullHouse(cards):
	if SameValue(cards[:3]) and SameValue(cards[3:]):
		return [7 , cards[0][0] , cards[4][0]]
	elif SameValue(cards[:2]) and SameValue(cards[2:]):
		return [7 , cards[4][0] , cards[0][0]]
	else:
		return False

def FourOfAKind(cards):
	if SameValue(cards[:4]):
		return [8 , cards[0][0] , cards[4][0]]
	elif SameValue(cards[1:]):
		return [8 , cards[4][0] , cards[0][0]]
	else:
		return False

def StraightFlush(cards):
	if Straight(cards) == False or Flush(cards) == False:
		return False
	return [9] + cards[0][0]

def RoyalFlush(cards):
	if StraightFlush(cards) == False:
		return False
	return [10 , 10]

#
value_dict = {}
for index , a in enumerate("23456789TJQKA"):
	value_dict[a] = index + 2
suit_dict = {}
for index , a in enumerate("HCSD"):
	suit_dict[a] = index
def Change(cards):
	for c in cards:
		yield (value_dict[c[0]],suit_dict[c[1]])
#
func = [RoyalFlush , StraightFlush , FourOfAKind, FullHouse , Flush , Straight , ThreeOfAKind , TwoPair , OnePair , HighCard]
def GetValue(cards):
	for f in func:
		ret = f(cards)
		if ret != False:
			return ret
cnt = 0
for line in open("054.in"):
	ab = line[:-1].split(' ')
	a = sorted(Change(ab[:5]))[::-1]
	b = sorted(Change(ab[5:]))[::-1]
	A = GetValue(a)
	B = GetValue(b)
	for i in xrange(6):
		if A[i] > B[i]:
			cnt += 1
			break
		elif A[i] < B[i]:
			break
print cnt

rankVals = {r:v for v,r in enumerate("23456789TJQKA")}
print rankVals
