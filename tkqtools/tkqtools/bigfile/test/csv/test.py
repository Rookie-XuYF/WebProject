import csv


def main():
    with open(
        "/home/nukeexplode/Desktop/tkqtools/tkqtools/bigfile/test/csv/test.csv",
        "r",
        encoding="utf-8",
    ) as fr:
        lines = fr.readlines()
        csv.Sniffer().sniff(lines[0])


if __name__ == "__main__":
    main()
