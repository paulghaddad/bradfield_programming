x = lambda x, y: lambda: x - y
result = (lambda one, question: one(46, question)())(x, 4)
