def read_file(filename: str) -> str:
        """
        This function reads a file and if there is one

        Returns:
            str: file content
        """
        try:
            with open(filename, 'r') as file:
                content: str = file.read().replace('\n', '')  
                return content
            
        except FileNotFoundError:
            print(f"Error: file '{filename}' not found")
            return ""