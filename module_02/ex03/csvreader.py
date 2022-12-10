class CsvReader:
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename)
        except FileNotFoundError:
            return None
        
        self.data = []
        self.header_row = None
        self.num_fields = None

        # Skip the top rows, if necessary
        for _ in range(self.skip_top):
            self.file.readline()

        # Read the header row, if necessary
        if self.header:
            self.header_row = self.file.readline().strip().split(self.sep)

        # Parse the remaining rows
        for line in self.file:
            fields = line.strip().split(self.sep)
            if self.num_fields is None:
                self.num_fields = len(fields)
            elif len(fields) != self.num_fields:
                # Inconsistent number of fields; file is corrupted
                return None
            self.data.append(fields)

        # Skip the bottom rows, if necessary
        for _ in range(self.skip_bottom):
            self.data.pop()

        return self

    def __exit__(self, type, value, traceback):
        try:
            self.file.close()
        except AttributeError:
            return None
        


    def getdata(self):
        return self.data

    def getheader(self):
        return self.header_row

