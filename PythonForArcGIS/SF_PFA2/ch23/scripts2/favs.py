import reportSTargs, sys

num = sys.argv[1]
color = sys.argv[2]

reportSTargs.printArc("""Your favorite positive number is {0}?
That's my favorite too!""".format(num))

reportSTargs.printArc("""Your favorite color is {0}?
Erm...I don't like {0}!""".format(color))
