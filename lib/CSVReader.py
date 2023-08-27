import csv

class CSVReader:
    def __init__(self, path: str) -> None:
        """
        This class will read the csv file and return the data

        :param path: str
        """
        self.path = path
        self.data = []
        self.headers = []
        self.read()

    def read(self) -> None:
        """
        This function will read the csv file and store the data in the data variable

        :return: None
        """
        with open(self.path, 'r') as file:
            # read the file
            reader = csv.reader(file)

            # get the headers
            self.headers = next(reader)

            # get the data from reader and append it to the data list
            for row in reader:
                self.data.append(row)
    
    def get_data(self) -> list:
        """
        This function will return the data

        :return: list
        """
        return self.data

    def get_headers(self) -> list:
        """
        This function will return the headers

        :return: list
        """
        return self.headers

    def get_row(self, index) -> list | None:
        """
        This function will return the row of the given index

        :param index: int
        :return: list|None
        """
        # check if the index is valid
        if index < 0 or index > len(self.data):
            return None

        return self.data[index]
