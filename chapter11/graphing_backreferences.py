"""
"Profiling memory" section example of creating reference
and backreference graphs of memory objects with objgraph.

"""
import objgraph


def example():
    x = []
    y = [x, [x], dict(x=x)]

    objgraph.show_refs(
        (x, y),
        filename='show_refs.png',
        refcounts=True
    )
    objgraph.show_backrefs(
        (x, y),
        filename='show_backrefs.png',
        refcounts=True
    )


if __name__ == "__main__":
    example()
