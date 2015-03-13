#!/usr/bin/python

import profligate
from profligate import sendemail

def test_search():
    print "Search test. Find the RRD files"
    profligate.search()
    pass

def test_trim():
    print "Trim test. Select recently updated files and cover memory and CPU."
    profligate.trim()
    pass

def test_average():
    print "Average test. Find the average of RRD file values."
    profligate.average()
    pass

def test_trigger():
    print "Trigger test. Find the average of RRD file values."
    profligate.trigger()
    pass

def test_unfloat():
    print "Search test. Convert memory values to a human readable format."
    assert (profligate.unfloat("1425285000:", "1.2786346416e+16") == "11Pb")
    assert (profligate.unfloat("1425281400:", "1.3437079461e+15") == "1.2Pb")
    assert (profligate.unfloat("1425283200:", "1.3069894702e+14") == "118Tb")
    assert (profligate.unfloat("1425285000:", "1.2786346416e+13") == "11Tb")
    assert (profligate.unfloat("1425286800:", "1.2472755382e+12") == "1.1Tb")
    assert (profligate.unfloat("1425281400:", "1.3437079461e+11") == "125Gb")
    assert (profligate.unfloat("1425283200:", "1.3069894702e+10") == "12Gb")
    assert (profligate.unfloat("1425285000:", "1.2786346416e+09") == "1.2Gb")
    assert (profligate.unfloat("1425286800:", "1.2472755382e+08") == "118Mb")
    assert (profligate.unfloat("1425281400:", "1.3437079461e+07") == "12Mb")
    assert (profligate.unfloat("1425283200:", "1.3069894702e+06") == "1.2Mb")
    assert (profligate.unfloat("1425285000:", "1.2786346416e+05") == "124Kb")
    assert (profligate.unfloat("1425286800:", "1.2472755382e+04") == "12Kb")
    assert (profligate.unfloat("1425281400:", "1.3437079461e+03") == "1.3Kb")
    assert (profligate.unfloat("1425283200:", "1.3069894702e+02") == "130bytes")
    assert (profligate.unfloat("1425285000:", "1.2786346416e+01") == "12bytes")
    assert (profligate.unfloat("1425286800:", "1.2472755382e+00") == "1bytes")
    print "float to human readable text test passed"

def test_sendemail():
    print "Search test"
    profligate.sendemail()
    pass

def test_writehtml():
    print "Search test"
    profligate.writehtml()
    pass
    
    
test_search()
test_trim()
test_average()
test_trigger()
test_unfloat()








