from cryptography.fernet import Fernet

filekey_path = 'filekey.key'

def generateKey():
    # key generation
    key = Fernet.generate_key()
    # string the key in a file
    with open(filekey_path, 'wb') as filekey:
        filekey.write(key)
        filekey.close()
        print(f'Done: New key in {filekey_path} is generated!\n')

def loadKey():
    try:
        # opening the key
        with open(filekey_path, 'rb') as filekey:
            key = filekey.read()
            filekey.close()
        # using the generated key
        return Fernet(key)
    except Exception:
        print(f"Error: {filekey_path} is required!\n")
        exit()