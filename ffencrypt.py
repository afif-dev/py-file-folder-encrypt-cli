import os, secrets, shutil
from filekey import load_key

def encrypt_file(args):
    # load key
    fernet = load_key()
    # split path
    filename, file_extension = os.path.splitext(args.path)
    # new filename
    new_file = filename + '_' + secrets.token_urlsafe(10) + file_extension 
    
    try:
        # opening the original file to encrypt
        with open(args.path, 'rb') as file:
            original = file.read()
            file.close()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(new_file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            encrypted_file.close()
            print(f'Done: File {new_file} is encrypted!\n')
            
    except Exception:
        print(f"Error: File {args.path} is invalid!\n")

def decrypt_file(args):
    # load key
    fernet = load_key()

    try:
        # opening the encrypted file
        with open(args.path, 'rb') as file:
            original = file.read()
            file.close()

        # decrypting the file
        decrypted = fernet.decrypt(original)

        # opening the file in write mode and
        # writing the decrypted data
        with open(args.path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
            decrypted_file.close()
            print(f'Done: File {args.path} is decrypted!\n')

    except Exception:
        print(f"Error: File {args.path} is invalid!\n")

def encrypt_folder(args):
    # load key
    fernet = load_key()
    # new folder name
    new_folder = args.path + '_' + secrets.token_urlsafe(10)
    # new folder zip name
    new_file_zip = new_folder + '.zip'
    # set zip file
    file_zip = args.path + '.zip'
    
    try:
        # zip folder
        print(f'In progress: Zip directory {args.path}')
        shutil.make_archive(args.path, 'zip', args.path)

        # opening the original file to encrypt
        with open(file_zip, 'rb') as file:
            original = file.read()
            file.close()
            # remove zip file
            os.remove(file_zip)

        # encrypting the file
        encrypted = fernet.encrypt(original)
        # opening the file in write mode and writing the encrypted data
        print(f'In progress: Encrypt zip file {file_zip}')

        with open(new_file_zip, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            encrypted_file.close()
            print(f'Done: File {new_file_zip} is encrypted!\n')
    
    except Exception:
        print(f"Error: Folder {args.path} is invalid!\n")

def decrypt_folder(args):
    # load key
    fernet = load_key()
    
    try:
        # opening the encrypted file
        print(f'In progress: Decrypt zip file {args.path}')
        with open(args.path, 'rb') as file:
            original = file.read()
            file.close()

        # decrypting the file
        decrypted = fernet.decrypt(original)

        # opening the file in write mode and
        # writing the decrypted data
        with open(args.path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
            decrypted_file.close()
            print(f'Done: File {args.path} is decrypted!\n')
    
    except Exception:
        print(f"Error: Zip file {args.path} is invalid!\n")
