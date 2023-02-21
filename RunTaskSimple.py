import sys
import os
SVFHOME = os.environ['SVFHOME']
sys.path.insert(0, SVFHOME + 'PyCaffeCUDA/pycaffe')
import SVFCore
CacheDir = SVFHOME + "Cache\\Default\\"
import time


if __name__ == "__main__":
    dir = sys.argv[1]
    GSVCapture = SVFCore.GSVCapture()
    GSVCapture.initialize(True)
    sys.stdout.flush()
    try:
        sys.stdout.write("task.started\n")
        sys.stdout.flush()
        GSVCapture.batchGetByID(dir)
        sys.stdout.write("task.finished\n")
        sys.stdout.flush()
    except Exception as err:
        sys.stdout.write(str(err) + "\n")
        sys.stdout.write("task.failed\n")
        sys.stdout.flush()