def solve():
  x, y, z = map(float, input().split())

  expressions = [
      "x^y^z",
      "x^z^y",
      "(x^y)^z",
      "(x^z)^y",
      "y^x^z",
      "y^z^x",
      "(y^x)^z",
      "(y^z)^x",
      "z^x^y",
      "z^y^x",
      "(z^x)^y",
      "(z^y)^x",
  ]

  values = [
      x ** (y ** z),
      x ** (z ** y),
      (x ** y) ** z,
      (x ** z) ** y,
      y ** (x ** z),
      y ** (z ** x),
      (y ** x) ** z,
      (y ** z) ** x,
      z ** (x ** y),
      z ** (y ** x),
      (z ** x) ** y,
      (z ** y) ** x,
  ]

  max_val = max(values)
  max_index = values.index(max_val)

  print(expressions[max_index])

solve()