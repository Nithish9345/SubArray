class SubArray:

    def function(self, array, l, r):

        for i in range(l, r):
            print(array[i], end = " ")

array = list(map(int, input().split()))
l, r = map(int, input().split())
object = SubArray()
object.function(array, l, r)