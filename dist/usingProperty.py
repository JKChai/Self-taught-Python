## Using Geek for Geek explanation - https://www.geeksforgeeks.org/python-property-function/

## Use to give property for a class and is commonly known to use as getter and setter
## which are all done with __set__, __get__, __deleter__ operator overloading

# Method 1: Using property function

class setClass:
    def __init__(self, value):
        self._value = value

    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value

    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, delValue, )


print('\n########### Method 1 ############\n')

# passing the value
x = setClass('Using built-in property as function')

## getting value - getter
print(x.value)

## setting value - setter
x.value = 'set new value'

## deleting value - deleter
del x.value

## Method 2: using @property decorator

print('\n########### Method 2 ############\n')

# Python program to explain property()
# function using decorator

class setClass:
	def __init__(self, value):
		self._value = value

	# getting the values
	@property
	def value(self):
		print('Getting value')
		return self._value

	# setting the values
	@value.setter
	def value(self, value):
		print('Setting value to ' + value)
		self._value = value

	# deleting the values
	@value.deleter
	def value(self):
		print('Deleting value')
		del self._value

# passing the value
x = setClass('Using built-in property as function')

## getting value - getter
print(x.value)

## setting value - setter
x.value = 'set new value'

## deleting value - deleter
del x.value
