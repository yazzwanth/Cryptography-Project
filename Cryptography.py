from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print("File not found.")
        return None

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    return encrypted_data, key

def decrypt_file(encrypted_data, key):
    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("Error:", str(e))
        return None

    return decrypted_data

def save_encrypted_file(encrypted_data, file_name):
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)

def menu():
    print("Choose an option:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def main():
    choice = menu()
    
    if choice == '1':
        file_path = input("Enter the path of the file you want to encrypt: ").strip('"')
        key = generate_key()
        encrypted_data, key = encrypt_file(file_path, key)
        if encrypted_data:
            encrypted_file_name = input("Enter the name for the encrypted file (with extension): ")
            save_encrypted_file(encrypted_data, encrypted_file_name)
            print("File encrypted and saved as", encrypted_file_name)
            print("Encryption Key:", key.decode())
    elif choice == '2':
        file_path = input("Enter the path of the file you want to decrypt: ").strip('"')
        key = input("Enter the key for decryption: ").encode()
        encrypted_data = None
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        if encrypted_data:
            decrypted_data = decrypt_file(encrypted_data, key)
            if decrypted_data:
                decrypted_file_name = input("Enter the name for the decrypted file (with extension): ")
                with open(decrypted_file_name, 'wb') as file:
                    file.write(decrypted_data)
                print("File decrypted and saved as", decrypted_file_name)
    else:
        print("Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()
