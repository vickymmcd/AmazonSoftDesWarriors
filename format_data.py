from data_scrape import get_data_dict


class Formatter:
    def __init__(self, url, file_name, data_file_name):
        '''
        Initializes the data Formatter object with
        a dictionary of data to be formatted.

        url: url of data to obtain from Tracktor
        file_name: name of file where id of data is saved
        data_file_name: name of file where data is saved
        NOTE: Only need data_file_name and data_file if they
        already exist, the other input can be an empty string.
        '''
        self.data_dict = get_data_dict(url, file_name, data_file_name)
        self.poly_func = 0

    def add_in_between_dates(self):
        self.data_dict
