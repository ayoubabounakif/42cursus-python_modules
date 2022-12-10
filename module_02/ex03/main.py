from csvreader import CsvReader
import sys 

if __name__ == "__main__":
    filename = sys.argv[1]
    # with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
    #     if reader == None:
    #         print("File is corrupted or missing")
    #     else:
    #         print(reader.getheader(), end = "\n")
    #         print(reader.getdata(), end = "\n\n")

    with CsvReader(filename, header = True, skip_top=0, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            # print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n")

# if __name__ == "__main__":
#     with CsvReader('good.csv') as file:
#         data = file.getdata()
#         header = file.getheader()

    # with CsvReader('bad.csv') as file:
    #     if file == None:
    #         print("File is corrupted")