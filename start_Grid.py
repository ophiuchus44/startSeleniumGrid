import os
import subprocess
import json
from multiprocessing import Process
import time


def startHub():
    os.system('python startHub.py')

def registerNode1():
    os.system('python registerNode1.py')

def registerNode2():
    os.system('python registerNode2.py')

#def registerDriver_Node1():
#    os.system('python registerDriver_node1.py')

#def registerDriver_Node2():
#    os.system('python registerDriver_node2.py')



if __name__ == '__main__':
    p1 = Process(target=startHub)
    p2 = Process(target=registerNode1)
    p3 = Process(target=registerNode2)
#    p4 = Process(target=registerDriver_Node1)
#    p5 = Process(target=registerDriver_Node2)
# start
    p1.start()
    # give quick delay for hub to launch
    time.sleep(3)

    p2.start()
    p3.start()
#    p4.start()
#    p5.start()
    #p1.join()
    #p2.join()
    #p3.join()

