def some_function(myList, myDict, myValue, myString, mytuple):
	myList.append(10)
	myDict['carlos'] = 10
	myValue = 0		#Won't change cuz we passed by value
	myString = 'carlos'	#Won't change cuz we passed by value
	myTuple = (0, 10)	#Won't change cuz we passed by value

someList = []
someDict = {}
someValue = -1
someString = ""
someTuple = ()

some_function(someList, someDict, someValue, someString, someTuple)

print(someList, someDict, someValue, someString, someTuple)
