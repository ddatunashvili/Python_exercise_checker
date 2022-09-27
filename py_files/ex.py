#__start__
def addition_1(a,b):
  return a + b

#__end__#__start__

def addition(n):
  return n + 1

#__end__#__start__

def convert(n):
  return n*60
#__end__#__start__

def cubes(a):
    return a ** 3

#__end__
#__start__
def dis(price, discount):
  percent = price*discount/100
  return int(price - percent)
print(dis(1500,50))

#__end__#__start__
def calc_age(age):
  return age*365

#__end__
#__start__
def string_int(string):
  return int(string)

#__end__#__start__
def find_perimeter(length, width):
  return  (length + width)*2
#__end__#__start__
def greeting(name):
    if name == "Murtaz":
        return "Hello, my Love!"
    else:
      return "Hello, " + name + "!"

#__end__#__start__
def stutter(text):
  return text[:2] + "... " + text[:2] + "... " + text+"?"

#__end__