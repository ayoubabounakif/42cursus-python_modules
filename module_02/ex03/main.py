from csvreader import CsvReader
import sys 

if __name__ == "__main__":
    filename = sys.argv[1]
    # with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
    #     if reader == None:
    #         print("File is corrupted or missing")
    #     else:
    #         print(reader.getheader(), end = "\n")
    #         for i in range(len(reader.getdata())):
    #             print(reader.getdata()[i], end = "\n")

    with CsvReader(filename, header=False, skip_top=0, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            for i in range(len(reader.getdata())):
                print(reader.getdata()[i], end = "\n")

    # with CsvReader('good.csv') as file:
    #     for i in range(len(file.getdata())):
    #         print(file.getdata()[i], end = "\n")

    # with CsvReader('bad.csv') as file:
    #     if file == None:
    #         print("File is corrupted")
    #     for i in range(len(file.getdata())):
    #         print(file.getdata()[i], end = "\n")