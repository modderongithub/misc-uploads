import subprocess

while True:
    exe_path = input("path >> ")  # Replace with your executable path
    if exe_path == "":
        break;
    try:
        result = subprocess.run(exe_path, shell=True, capture_output=True, text=True)
        print(result.stdout if result.returncode == 0 else result.stderr)
    except Exception as e:
        print("Execution failed:", e)
