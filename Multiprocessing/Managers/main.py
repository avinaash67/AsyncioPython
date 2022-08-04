from multiprocessing import Process, Manager, current_process


def worker(list1, num):
    """ Worker process that appends number to the manager-list
    Args:
        list1: Shared manager-list. (This list by the manager class can be shared between multiple processes)
        num: Number to be appended to the manager list.
    Returns:
    """
    list1.append(num)
    print("list by", current_process().name,list1)



if __name__ == '__main__':
    
    mgr = Manager()  # Manager object created from Manager class
    list1 = mgr.list()  # Special type of list (Manager-list). 

    process1 = Process(name="worker1", target=worker, args=(list1,10))
    process2 = Process(name="worker2", target=worker, args=(list1,20))

    process1.start()
    process2.start()

    print("Final list",list1)