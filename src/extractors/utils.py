thonimport json

def load_json(filename):
    """
    Loads data from a JSON file.
    Parameters:
        filename (str): The name of the file to load.
    Returns:
        dict: Loaded data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
    
def save_json(data, filename):
    """
    Saves data to a JSON file.
    Parameters:
        data (dict): Data to be saved.
        filename (str): The name of the file to save the data.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)