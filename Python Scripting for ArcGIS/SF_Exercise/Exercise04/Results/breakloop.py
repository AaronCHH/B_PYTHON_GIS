# Name: <your name>
# Date: <current date>
# Description: This script demonstrates how to break a loop

from math import sqrt
for n in range(1000, 0, -1):
	root = sqrt(n)
	if root == int(root):		# This evaluates whether the root is an integer
		print root
		break