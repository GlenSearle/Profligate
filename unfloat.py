import time
import unittest


def unfloat(UnixTime, FloatString):
    FloatPower = int(FloatString[15:16])
    FloatValue = float(FloatString[0:-5])*(10**FloatPower)
    UnixTime = UnixTime[0:9]
    
    if FloatPower > 15:
        FloatValue = FloatValue / (1024**4)
        ScaleText = "Tb"
    elif FloatPower > 11:
        FloatValue = FloatValue / (1024**3)
        ScaleText = "Gb"
    elif FloatPower > 7:
        FloatValue = FloatValue / (1024**2)
        ScaleText = "Mb"
    elif FloatPower > 3:
        FloatValue = FloatValue / 1024
        ScaleText = "Kb"
    else:
        ScaleText = "bytes"
    
    Output = "str(int(FloatValue)) + ScaleText"
    print Output
    #print SimpleDate(UnixTime, tz='utc').date
    return Output


"""
# Here's our "unit tests".
class UnfloatTests(unittest.TestCase):

    UnixTime = "1425317400:"
    FloatString = "5.8821073124e+08"

    def testOne(self):
        self.failUnless(Unfloat(UnixTime, FloatString))

    def testTwo(self):
        self.failIf(Unfloat(UnixTime, FloatString))

def main():
    unittest.main()

if __name__ == '__main__':
    import unittest
    main()
    
    """