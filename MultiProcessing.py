import logging
import multiprocessing
from multiprocessing import Pool
# Python Multiprocessing example

logging.basicConfig(filename='logfile.log',level=logging.DEBUG)

# print/log numbers
def spawn(num, num2):
    print('Spawn # {} {}'.format(num, num2))
    logging.info('spawn {} + {}'.format(str('str'), str('sst')))

# return a double and log it
def job(num):
    return num * 2
    logging.info('job {} + {}'.format(str('str'), str('sst')))

#Main function of the Program
if __name__ == '__main__':
    for i in range(500):
        #multiprocessing part
        p = multiprocessing.Process(target=spawn, args=(i, i+1))
        p.start()
    logging.info('main {} + {}'.format(str('str'), str('sst')))
    #creating a pool for execution
    p = Pool(processes=20)
    data = p.map(job, [i for i in range(500)])
    p.close()
    print(data)