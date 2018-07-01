class Permutation:
    
    @staticmethod
    def printAllPermutation(str_, res):
        if not str_:
            print(res)
            return
        for chr_ in str_:
            strCpy = str_[:]
            strCpy.remove(chr_)
            Permutation.printAllPermutation(strCpy, res + chr_)

if __name__ == '__main__':
    Permutation.printAllPermutation(['a', 'b', 'c'], '')
