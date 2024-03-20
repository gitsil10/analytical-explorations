"""
@gitsil10
@file process_data.py
@brief A class to process data
@details A class to process data
@version 0.1
@date 2024-03-20
@dependencies
os
"""
#imports
from os import path

#class
class ProcessData:
    """
    @brief A class to process data
    @param data (str): The data to process
    @param paths (dict): The paths to the raw, processed, and output data
    @return (ProcessData): The ProcessData object
    """
    def __init__(self):
        self.paths:dict = {
            "output": "data/output",
            "processed": "data/processed",
            "raw": "data/raw"
            }

    def get_path(self) -> dict:
        """
        @brief Get the paths dictionary
        @return (dict): The paths dictionary

        @example
        get_path()

        @details
        Return the paths dictionary

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.paths
    
    def path_raw(self) -> str:
        """
        @brief Get the path to the raw data
        @return (str): The path to the raw data
        """
        return self.get_path()["raw"]
    
    def path_processed(self) -> str:
        """
        @brief Get the path to the processed data
        @return (str): The path to the processed data
        """
        return self.get_path()["processed"]
    
    def path_output(self) -> str:
        """
        @brief Get the path to the output data
        @return (str): The path to the output data
        """
        return self.get_path()["output"]
    
    def write_data(self, path_name:str, file_name:str, data:str) -> bool:
        """
        @brief Write data to a file
        @param path_name (str): The path to the file
        @param file_name (str): The file name
        @param data (str): The data to write
        @return (bool): True if the file was written, False otherwise

        @example
        write("data/output", "output.txt", "Hello, World!")

        @details
        If the path exists and the data is not empty, write the data to the file.
        If the file exists, append the data to the file. 
        Otherwise, create the file and write the data to it.

        @note
        Time: O(1)
        Space: O(1)
        """
        if path.isdir(path_name) and data and len(data) > 0:
            with open(
                f'{path_name}/{file_name}', 
                "a" if path.exists(f"{path_name}/{file_name}") else "w"
                ) as f:
                f.write(data)
            return True
        return False

    def write_raw(self, file_name:str, data:str) -> bool:
        return self.write_data(self.path_raw(), file_name, data)

    def write_processed(self, file_name:str, data:str) -> bool:
        return self.write_data(self.path_processed(), file_name, data)

    def write_output(self, file_name:str, data:str) -> bool:
        return self.write_data(self.path_output(), file_name, data)