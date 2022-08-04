## Pipe

It is a data structure, which is used to communicate between processes. The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex(two way)[1].

- It returns a pair of connection objects that represent the two ends of pipe.
- Every object has two methods – send() and recv(), to communicate between processes[1].

### Points to note:
- **Pipe can have only 2 endpoints whereas a Queue can have multiple producers and conumers.**
- A Queue can be used when there are multiple processes communicating with each other. 
- Pipe is much faster than a queue, this is because a Queue() is built on top of Pipe() [2]


### References
1. Tutorials Point, https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_processes_intercommunication.htm
2. Indian Pythonista - youtube, https://www.youtube.com/watch?v=5ff4_YK83fQ&t=15s&ab_channel=IndianPythonista