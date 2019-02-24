import logging
import multiprocessing
from multiprocessing import Pool
# Python Multiprocessing example

logging.basicConfig(filename='logfile.log',level=logging.DEBUG)

def spawn(num, num2):
    print('Spawn # {} {}'.format(num, num2))
    logging.info('spawn {} + {}'.format(str('str'), str('sst')))


def job(num):
    return num * 2
    logging.info('job {} + {}'.format(str('str'), str('sst')))

if __name__ == '__main__':
    for i in range(500):
        p = multiprocessing.Process(target=spawn, args=(i, i+1))
        p.start()
    
    logging.info('main {} + {}'.format(str('str'), str('sst')))
    p = Pool(processes=20)
    data = p.map(job, [i for i in range(500)])
    p.close()
    print(data)