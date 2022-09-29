import invoke

@invoke.task
def clean(c):
    """ Remove any built objects """
    for pattern in ["*.o", "*.so"]:
        c.run("rm -rf {}".format(pattern))


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task
def build_heap(c):
    """ Build the shared library for the sample C code """
    print_banner("Building C Library")
    invoke.run("gcc -c -Wall -fpic testheap.c -I /usr/include/python3.10")
    invoke.run("gcc -shared -o testheap.so testheap.o")
    print("* Complete")