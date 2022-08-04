""" Pipe example for IPC in python"""

from multiprocessing import Pipe, Process

def send_msgs(conn,msgs):
    """ Sending process. This sends messages through one end of the pipe
    Args:
        conn: front_end of the pipe
        msgs: messages to be sent
    Returns: 
    """
    for msg in msgs:
        conn.send(msg)
    conn.close()

def recv_msgs(conn):
    """Receiving process. Process to recieve messages from other end of the pipe
    Args:
        conn: back_end of the pipe
    Returns:
    """
    while 1:
        msg =conn.recv()
        if msg == "end":
            break
        print(msg)


if __name__ == '__main__':
    msgs = ["Hello!","how", "are", "you", "end"]
    front_end, back_end = Pipe()

    process1 = Process(target=send_msgs, args=(front_end,msgs))
    process2 = Process(target=recv_msgs, args=(back_end,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()