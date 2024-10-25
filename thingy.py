import ctypes
import os

# Define necessary constants
CREATE_NEW_CONSOLE = 0x00000010
CREATE_SUSPENDED = 0x00000004

# Define a structure for process information
class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", ctypes.c_void_p),
        ("hThread", ctypes.c_void_p),
        ("dwProcessId", ctypes.c_ulong),
        ("dwThreadId", ctypes.c_ulong)
    ]

# Define a structure for startup information
class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ("cb", ctypes.c_ulong),
        ("lpReserved", ctypes.c_char_p),
        ("lpDesktop", ctypes.c_char_p),
        ("lpTitle", ctypes.c_char_p),
        ("dwX", ctypes.c_ulong),
        ("dwY", ctypes.c_ulong),
        ("dwXSize", ctypes.c_ulong),
        ("dwYSize", ctypes.c_ulong),
        ("dwXCountChars", ctypes.c_ulong),
        ("dwYCountChars", ctypes.c_ulong),
        ("dwFillAttribute", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("wShowWindow", ctypes.c_short),
        ("cbReserved2", ctypes.c_ushort),
        ("lpReserved2", ctypes.POINTER(ctypes.c_ubyte)),
        ("hStdInput", ctypes.c_void_p),
        ("hStdOutput", ctypes.c_void_p),
        ("hStdError", ctypes.c_void_p)
    ]

def run_exe(exe_path):
    if not os.path.isfile(exe_path):
        raise FileNotFoundError(f"Executable not found: {exe_path}")

    # Initialize startup info and process info structures
    startup_info = STARTUPINFO()
    process_info = PROCESS_INFORMATION()
    startup_info.cb = ctypes.sizeof(STARTUPINFO)

    # Create a new process for the executable
    result = ctypes.windll.kernel32.CreateProcessW(
        exe_path,              # Path to the executable
        None,                  # Command line arguments
        None,                  # Process handle not inheritable
        None,                  # Thread handle not inheritable
        False,                 # Set handle inheritance to FALSE
        CREATE_NEW_CONSOLE | CREATE_SUSPENDED,  # Creation flags
        None,                  # Use parent's environment block
        None,                  # Use parent's starting directory
        ctypes.byref(startup_info),  # Pointer to startup info
        ctypes.byref(process_info)   # Pointer to process info
    )

    if not result:
        raise RuntimeError(f"CreateProcess failed, error code: {ctypes.GetLastError()}")

    print(f"Process created successfully: PID {process_info.dwProcessId}")

    # Resume the thread to start execution
    ctypes.windll.kernel32.ResumeThread(process_info.hThread)

    # Close handles (not necessary for the demo, but good practice)
    ctypes.windll.kernel32.CloseHandle(process_info.hThread)
    ctypes.windll.kernel32.CloseHandle(process_info.hProcess)

# Example usage
exe_path = r"UltimMC\UltimMC.exe"  # Replace with your executable path
run_exe(exe_path)
