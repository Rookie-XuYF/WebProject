from multiprocessing import Pool
from time import sleep
from string import Template


def worker():
    sleep(5)


def main():
    t = Template("hello $name")
    print(t.substitute(name="w`orld"))


if __name__ == "__main__":
    main()
