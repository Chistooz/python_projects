sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, None,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]


def count_sheep(sheep):

    count = 0
    for i in sheep:
        if i:
            count += 1
        else:
            continue

    return count


print(count_sheep(sheep))
