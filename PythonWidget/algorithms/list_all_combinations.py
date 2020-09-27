 def comb(objs):
    ret = []
    if len(objs) == 1:
        return ["".join(map(str, objs[0]))]
    elif len(objs) == 2:
        first, second = objs
        for f in first:
            for s in second:
                ret.append("".join(map(str, [f, s])))
        return ret
    elif len(objs) > 3:
        first, second, *extra = objs
        new = []
        for f in first:
            for j in second:
                new.append("".join(map(str, [f, j])))
        return comb([new, *extra])
    else:
        first, second, third = objs
        for f in first:
            for s in second:
                for t in third:
                    ret.append("".join(map(str, [f, s, t])))
        return ret
        
if __name__ == "__main__":
  test = [
    [[1]],
    [[1,2,3]],
    [[1,2,3], [2, 3]],
    [[1], [2, 3], [3, 4], [4, 5]]
  ]
  for t in test:
    print(comb(t))
