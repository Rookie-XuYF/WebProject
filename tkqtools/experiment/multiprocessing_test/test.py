import multiprocessing


def f(name):
    print("hello", name)


def main():
    p = multiprocessing.Process(target=f, args=("world",))
    p.start()
    p.join()


if __name__ == "__main__":
    main()
