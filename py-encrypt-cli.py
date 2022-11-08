import argparse
from cryptography.fernet import Fernet
from filekey import generateKey
from ffencrypt import encryptFile, decryptFile, encryptFolder, decryptFolder

def main():
    startuptxt = """
    ______ _  __         ___        ______        __     __               ______                                  __     ______ __     ____
   / ____/(_)/ /___     ( _ )      / ____/____   / /____/ /___   _____   / ____/____   _____ _____ __  __ ____   / /_   / ____// /    /  _/
  / /_   / // // _ \   / __ \/|   / /_   / __ \ / // __  // _ \ / ___/  / __/  / __ \ / ___// ___// / / // __ \ / __/  / /    / /     / /  
 / __/  / // //  __/  / /_/  <   / __/  / /_/ // // /_/ //  __// /     / /___ / / / // /__ / /   / /_/ // /_/ // /_   / /___ / /___ _/ /   
/_/    /_//_/ \___/   \____/\/  /_/     \____//_/ \__,_/ \___//_/     /_____//_/ /_/ \___//_/    \__, // .___/ \__/   \____//_____//___/   
                                                                                                /____//_/                                  
      
Desc: encrypt & decrypt file or folder (Keep your secret forever!)
Author: afif-dev https://github.com/afif-dev
    """
    print(startuptxt)

    parser = argparse.ArgumentParser(prog='py-encrypt-cli', description='Encrypt & decrypt file or folder.')
    parser.add_argument('path', metavar='file_folder_path', type=str, nargs='?', default=None, help='file or folder path')
    parser.add_argument('-gk', '--gen-key', choices=['true', 'false'], default='false', help='generate file key')
    parser.add_argument('-pt','--path-type', choices=['file', 'folder'], default='file', help='path type')
    parser.add_argument('-et', '--encryption-type', choices=['encrypt', 'decrypt'], default='encrypt', help='encryption type')
    
    args = parser.parse_args()
    
    if args.gen_key == 'true':
        generateKey();
    elif args.path != None and args.path_type == 'file' and args.encryption_type == 'encrypt':
        print("# Encrypt File")
        encryptFile(args)
    elif args.path != None and args.path_type == 'file' and args.encryption_type == 'decrypt':
        print("# Decrypt File")
        decryptFile(args)
    elif args.path != None and args.path_type == 'folder' and args.encryption_type == 'encrypt':
        print("# Encrypt Folder")
        encryptFolder(args)
    elif args.path != None and args.path_type == 'folder' and args.encryption_type == 'decrypt':
        print("# Decrypt Folder")
        decryptFolder(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()