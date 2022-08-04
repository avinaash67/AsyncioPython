## Manager

Manager is a class of multiprocessing module that provides a way to coordinate shared information between all its users(In this case users are other processes). A manager object controls a server process, which manages shared objects and allows other processes to manipulate them. In other words, managers provide a way to create data that can be shared between different processes. [1]

Through the manager class object lists, dictionaries and queues can be shared. These Manager objects are held by the manager-server-process that allows other processes to modify it.

### References
1. Tutorials point, https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_processes_intercommunication.htm