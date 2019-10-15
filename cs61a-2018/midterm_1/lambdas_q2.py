x = lambda x: lambda y: x(y)
result = (lambda fair, dice: x(fair)(dice))(lambda fair: fair == 3, 3)
