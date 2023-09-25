# generators create iterable to control memeory allocation (on the fly generate)
# iterable only once

def gen(n):
    for i in range(n):
        yield i;

g = gen(3000)
print(g)

# print(g._next_())
for i in g:
    print(i)
 