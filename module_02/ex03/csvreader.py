class CsvReader:

    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.file = None

    def __enter__(self, method):
        self.file = open(self.filename, method)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        
        
            
    