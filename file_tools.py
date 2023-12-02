def read_file(text_file: str)->str:
    """
    Open a file and return a list[str]
    """
    
    with open(text_file, 'r') as text_read:

        text = text_read.read()

         
    return text