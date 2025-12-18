from pathlib import Path

def load_input_line(filename: str, strip_empty: bool=True) -> str:
    """
    Load the first line of the input file for Advent of Code challenges.

    Parameters:
    - filename (str): The filename relative to the 'inputs/' folder
    - strip_empty (bool): If True, removes empty lines

    Returns:
    - str: the first input line
    """
    file_path = Path("inputs") / filename

    # Read the file
    with file_path.open() as f:
        line = f.readline().strip()

    return line

def load_input_line_int(filename: str, strip_empty: bool = True) -> int:
    """
    Load the first line of the input file for Advent of Code challenges and convet it to an integer.

    Parameters:
    - filename (str): The filename relative to the 'inputs/' folder
    - strip_empty (bool): If True, removes empty lines

    Returns:
    - int: the first input line as an integer
    """
    line = load_input_line(filename, strip_empty)
    return int(line)

def load_input_list(filename: str, strip_empty: bool=True) -> list[str]:
    """
    Load the input file for Advent of Code challenges.

    Parameters:
    - filename (str): The filename relative to the 'inputs/' folder
    - strip_empty (bool): If True, removes empty lines

    Returns:
    - list[str]: A list of input lines as strings
    """
    file_path = Path("inputs") / filename

    # Read the file
    with file_path.open() as f:
        lines = f.read().splitlines()

    # Optional: remove empty lines
    if strip_empty:
        return [line for line in lines if line.strip() != ""]

    return lines    

def load_input__list_int(filename: str, strip_empty: bool=True) -> list[int]:
    """
    Load the input file for Advent of Code challenges and convert lines to integers.

    Parameters:
    - filename (str): The filename relative to the 'inputs/' folder
    - strip_empty (bool): If True, removes empty lines

    Returns:
    - list[int]: A list of input lines as integers
    """
    lines = load_input_list(filename, strip_empty)
    return [int(line) for line in lines]

def load_groups(filename: str) -> list[list[str]]:
    """
    Load the input file and split it into groups separated by empty lines.

    Parameters:
    - filename (str): The filename relative to the 'inputs/' folder

    Returns:
    - list[list[str]]: A list of groups, where each group is a list of strings
    """
    file_path = Path("inputs") / filename

    with file_path.open() as f:
        raw_groups = f.read().strip().split("\n\n")

    return [group.splitlines() for group in raw_groups]

def load_groups_int(filename: str) -> list[list[int]]:
    """
    Load the input file and split it into groups separated by empty lines,
    converting each line to an integer.

    Parameters:
    - filename (str): The filename relative to the 'inputs/' folder

    Returns:
    - list[list[int]]: A list of groups, where each group is a list of integers
    """
    string_groups = load_groups(filename)
    return [[int(line) for line in group] for group in string_groups]