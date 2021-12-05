# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()

#     return inner


# @make_pretty
# def ordinary_fun():
#     print("Am ordinary")


# ordinary_fun()


def divider(func):
  def inner(a,b):
      print("dividing {} by {}".format(a,b))
      if a == 0:
          print("it is not divisible by 0")
          return
      return func(a, b)

  return inner

@divider
def Sdivider(a,b):
    print(a/b)

Sdivider(0,4)

