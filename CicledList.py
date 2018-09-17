import copy


class CicledList(list):
    """If index put of range -> go to other side of list"""
    def __init__(self, seq=()):
        super().__init__(seq)

    def __getitem__(self, item):
        # print('item: ', item, 'Res: ', len(self) % (item + 1))
        return list.__getitem__(self, item % len(self))

    def copy(self):
        # print('!!! copy')
        return CicledList(copy.deepcopy(self))
        # return CicledList(super().copy())

# test2 = CicledList()
# test2.append(1)
# test2.append(2)
# test2.append(3)
# test2.append(4)
# test2.append(5)
#
# for i in range(len(test2) * 2):
#     print(i, test2[i])
#
# print(help(CicledList))
