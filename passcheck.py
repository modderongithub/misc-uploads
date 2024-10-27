import subprocess

def verify_password(admin_username, password):
    try:
        command = f'echo {password} | runas /user:{admin_username} "cmd /c whoami"'
        result = subprocess.run(command, shell=True, text=True, input=password, capture_output=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

# Example usage
admin_username = "AdminUsername"
password = "Password123"

if verify_password(admin_username, password):
    print("Password is correct.")
else:
    print("Password is incorrect.")
