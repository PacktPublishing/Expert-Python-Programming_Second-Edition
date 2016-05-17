"""
"Multiprocessing" section example showing how
to spawn new process using os.fork on POSIX
systems.

"""
import os

pid_list = []


def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()

    if child_pid == 0:
        pid_list.append(os.getpid())
        print()
        print("CHLD: hey, I am the child process")
        print("CHLD: all the pids i know %s" % pid_list)

    else:
        pid_list.append(os.getpid())
        print()
        print("PRNT: hey, I am the parent")
        print("PRNT: the child is pid %d" % child_pid)
        print("PRNT: all the pids i know %s" % pid_list)


if __name__ == "__main__":
    main()
