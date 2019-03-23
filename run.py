import sys,os
sys.path.append(os.getcwd())
from OctoPrintUtil import *
from GoogleAPI_Util import *

report = getOctoPrint_PrintLogs()
'''TESTS
for row in report:
        print(row)
'''
buildOctoPrint_PrintLogs(report,"File Logs")
    
