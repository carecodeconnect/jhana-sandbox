def replace_strings_in_file(input_file_path, output_file_path):
    # Define the strings to search for and their replacements
    replacements = {
        '{"messages": [{"role": "user"': '{"messages": [{"role": "system", "content": "You are a Jhana meditation assistant that guides the user through a Jhana meditation and answers their questions."}, {"role": "user",'
         }
    
    # Read the input file
    with open(input_file_path, 'r') as file:
        file_contents = file.read()

    # Perform the replacements
    for search_string, replacement_string in replacements.items():
        file_contents = file_contents.replace(search_string, replacement_string)

    # Write the modified content to the output file
    with open(output_file_path, 'w') as file:
        file.write(file_contents)

# Example usage
input_file_path = '11_curate_training_dataset_user_agent_transformed_openai_user+assistant.txt'  # Update this to the path of your input file
output_file_path = '11_curate_training_dataset_user_agent_transformed_openai_system+user+assistant.txt'  # Update this to the desired path for the output file

replace_strings_in_file(input_file_path, output_file_path)
