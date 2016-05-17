"""
"Multiprocessing" section example showing how
to use pipes from `multiprocessing` module
as communication channel.

"""
from multiprocessing import Process, Pipe


class CustomClass:
    pass


def work(connection):
    while True:
        instance = connection.recv()

        if instance:
            print(
                "CHLD: recv: {}".format(instance)
            )

        else:
            return


def main():
    parent_conn, child_conn = Pipe()

    child = Process(target=work, args=(child_conn,))

    for item in (
        42,
        'some string',
        {'one': 1},
        CustomClass(),
        None,
    ):
        print(
            "PRNT: send: {}".format(item)
        )
        parent_conn.send(item)

    child.start()
    child.join()


if __name__ == "__main__":
    main()
