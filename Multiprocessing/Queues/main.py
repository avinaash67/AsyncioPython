from concurrent.futures import process
from multiprocessing import Process, Queue

def function(queue1):
    """Function that inserts value into the queue"""
    queue1.put([42, None, 'hello'])

def main():
   """Main function"""
   queue1 = Queue()  # initiating a queue
   process1 = Process(target = function, args = (queue1,)) # Args are passed as tuple
   
   process1.start()
   print (queue1.get())  # Reading from the queue

if __name__ == '__main__':
   main()