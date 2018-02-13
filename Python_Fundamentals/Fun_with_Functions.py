def odd_even(num):
    for i in range(1,2000):
        if i % 2 == 1:
            print "The number is " + str(i) + ". " + "This is an odd number."
        else:
            print "The number is " + str(i) + ". " + "This is an even number."

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
arr_1 = [2,4,10,16]
arr_2 = multiply(arr_1, 5)
print arr_2

def layered_multiples(arr):
  new_arr = []
      for x in range (len(arr)):
          new_arr.append[(1)]
          a = new_arr[x]
          while a > 0:
              new_arr[x].append(x/x)
              a -= 1
  # print new_arr
  return new_arr
beta = layered_multiples(multiply([2,4,5],3))
print beta
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
