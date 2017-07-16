#! /usr/bin/python

# import sys

# def main():
# 	print 'Hello there ', sys.argv[1]

# if __name__ == '__main__':
# 	main()

# print len(sys.argv)
def repeat(s, exclaim):
	result = s*3
	if exclaim:
		result += '!!!'
	return result

repeat("ha", "exclaim")