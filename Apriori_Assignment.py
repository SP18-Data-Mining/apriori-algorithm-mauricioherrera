transDatabase = [ ['a','c','e'], ['b','c','e'],
				  ['a','b','c','e'], ['b','e','d'] ]

# This holds the itemsets that frequently occur in the database
# A list of sets
frequencyList = [ ]

# A candidate list - the cardinality of Fk with each element in the database
# A list of sets 
candidateList = []


# 1 initialize the frequencyList 
# Find the longest set in the database
maxSetLength = 0
for currentSet in transDatabase :
	if (len(currentSet) > maxSetLength) :
		maxSetLength = len(currentSet)

# frequencyList =  [  {}, {}, ... maxSetLength] where all the sets are empty
for index in range(maxSetLength) :
	frequencyList.append(set())


# generate C(1)-- candidateList1  and F(1) frequencyList
candidateMap = {}
for currentSet in transDatabase :
	for element in currentSet :
#		print(element)
#		candidateMap[element] = 1
		if element in  candidateMap.keys() :
			candidateMap[element] = candidateMap[element] + 1
		else :
			candidateMap[element] = 1


removeList = []
# Removing all the frequency of 1 from candidateMap
f1 = { i:candidateMap[i]  for i in candidateMap if candidateMap[i] != 1 }


k_1Set = f1.keys()

for element in k_1Set :
	print(element)



frequencyList.append(f1)  #  frequentList[0] are the single frequent items
removeList.append(  { i:candidateMap[i]  for i in candidateMap if candidateMap[i] == 1 } )

#print(f1)
#print(removeList)


#k = 0
#while len(frequentList[k]) != 0 :
	# Generating and filtering C (k+1), by doing this we create  F (k+1)	
	
		
F_0  =  { 'a', 'b', 'c', 'e', 'f' }


F_k  = [ { 'a','b','c' }, {'a','e','f'}, { 'b','c','e'}, {'a','f','c' } ]


# Here k represents the number of elements within Fk
def multiplySet(fk,f0,k) :
	# We want to union the cartesian products betwen the two sets.
	ckplus1 = []
	for f0Element in f0 :
		for ithSet in fk :
			# This option is for the full credit, not taking the hash
			result = ithSet.union(f0Element)
			if len(result) == k+1 :
				checkDuplicateSet(ckplus1,result)

	return ckplus1



# c is something like [ { ... }, { .... } ...  ]
# result is :  { .... }
def checkDuplicateSet(c,result) :
	duplicate = False
	for element in c :
		if element == result :
			duplicate = True
		
	if duplicate == False :
		c.append(result) 

c = multiplySet(F_k,F_0,3)
print(c)

				


	




	

 


