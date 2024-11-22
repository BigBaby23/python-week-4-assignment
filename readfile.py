def modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content from '{input_file}' has been modified and written to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage
input_file = 'input.txt'
output_file = 'output.txt'

# Call the function
modify_file(input_file, output_file)

