import subprocess

def pseudo_command_prompt():
    print("command prompt (real fr!) | cd cmd dont do ass")
    
    while True:
        # Prompt user for a command
        command = input("cmd~")

        # Exit loop if user types 'exit'
        if command.lower() == 'exit':
            print("Exiting pseudo command prompt.")
            break

        try:
            # Execute the command and capture the output
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Print the command's output or error
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print("Error:", result.stderr)
                
        except Exception as e:
            print("An error occurred:", e)

# Run the pseudo command prompt
pseudo_command_prompt()
