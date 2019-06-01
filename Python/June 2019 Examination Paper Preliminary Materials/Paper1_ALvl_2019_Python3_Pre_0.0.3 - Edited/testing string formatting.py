def testPrint():
    header = ""
    header += "%-5s" % ("ID",)
    header += "%-12s" % ("NAME",)
    header += "%-64s" % ("DESC",)
    header += "%d" % (10,)
    print(header)

if __name__ == '__main__':
    testPrint()