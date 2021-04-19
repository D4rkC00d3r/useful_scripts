import time
from multiprocessing import Pool
from tqdm import tqdm

class Poolprgress:
    def __init__(self):
        self.pbar_chunk = 30
        self.cores = 1

    def square(self, n):
        square = n * n
        time.sleep(.5) # Make it take longer!
        return square 

    def main(self):
        t1 = time.time() # Record time at start of job.
        with Pool(processes=self.cores) as p:
            with tqdm(total=self.pbar_chunk) as pbar:
                for i, _ in enumerate(p.imap_unordered(self.square, range(self.pbar_chunk))):
                    pbar.update()
                    # close() and join() not required as used 'with'
        # Record time at the end and subtract the time from the start to show total time taken for job.            
        print('Time taken: {}'.format(time.time() - t1))

if __name__ == '__main__':
    poolprogress = Poolprgress()
    poolprogress.main()
