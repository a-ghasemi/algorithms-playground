import time
import numpy as np


def print_mat(mat, sep=' | '):
    mx = len(str(np.max(mat)))
    mn = len(str(np.min(mat)))
    mx = max(mn, mx)
    sep2 = sep + mx * ' '
    for row in mat:
        print(''.join(str(x).rjust(mx) for x in row).lstrip(sep.strip(' ')))
        # print(''.join(sep2[:mx - len(str(x)) + len(sep)] + str(x) for x in row).lstrip(sep.strip(' ')))


def str_to_mat(str):
    arr = list()
    rows = str.rstrip().splitlines()
    for row in rows:
        if len(row):
            arr.append(list(map(int, row.rstrip().split())))
    return arr

# SAMPLE
# s = '''
# 1 2 3
# 1 1 0
# 1 200 1
# 1 0 1
# '''
#
# ar = str_to_mat(s)
# print_mat(ar, ' ')


class Timer:
    '''
    Timer Class to find process time
    '''
    def __init__(self, start = False):
        self.debug = False
        self.start_time = 0
        self.calculated_time = 0
        self.state = 'initiated'
        if start: self.start()

    def start(self):
        if self.state == 'stopped': self.start_time = time.process_time()
        self.state = 'started'
        if self.debug: print('+ Timer Started')

    def stop(self):
        self.state = 'stopped'
        self.calculated_time = time.process_time() - self.start_time
        self.start_time = 0
        if self.debug: print('+ Timer Stopped')

    def pause(self):
        self.state = 'paused'
        self.calculated_time = time.process_time() - self.start_time
        if self.debug: print('+ Timer Paused')

    def read(self):
        return self.calculated_time

    def show(self):
        '''
        Prints the calculated time in output
        :return: None
        '''
        print("Elapsed time: --- %.5f seconds ---" %  self.calculated_time)

