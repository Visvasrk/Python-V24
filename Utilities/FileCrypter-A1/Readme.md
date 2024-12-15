# FileCrypter-A1 (or) Crypto-Grapher-A1

## Overview

Crypto-Grapher is a Python-based file encryption and decryption tool designed to securely encrypt and decrypt files or entire directory structures. It uses the `cryptography.fernet` module for encryption, providing strong encryption with password-based key management. This tool allows for encrypting or decrypting individual files, directories, and entire directory trees. The password used for encryption/decryption is stored as a one-time password (OTP), which means it is required only once per session.

**IMPORTANT:** Ensure that you run this file in a safe and isolated directory to avoid accidental data loss. Be very cautious with the password you set, as losing it will make the encrypted files irreversibly corrupted.

## Features

- **Encrypt/Decrypt Files in Directory Tree**: Encrypt or decrypt all files in a directory and its subdirectories.
- **Encrypt/Decrypt Files in a Directory**: Encrypt or decrypt all files in a specific directory.
- **Encrypt/Decrypt Specific File**: Encrypt or decrypt a specific file.
- **Key Management**: Store and retrieve encryption keys (passwords) for decryption.
- **Password Protection**: Each encryption operation is protected by a one-time password (OTP).

## File Structure

The tool uses a special key directory to store the passwords used for encryption. The keys are saved in files with the given password as the filename, and the encryption keys are associated with these passwords.

### Key Directory

By default, the tool uses `.Crypter/files/keys/` for storing keys. You can modify the path as needed.

## Important Notes

- **One-Time Passwords (OTPs):** Each encryption operation uses a unique password (OTP). Be sure to remember or securely store the password, as it will be required for decryption.
- **Irreversible Encryption:** If you lose the password for a file or directory, the encryption cannot be reversed. The encrypted files will remain inaccessible.
- **File Integrity:** Ensure that the files you are encrypting are not already corrupted before encryption, as encryption will also lock any existing data.
- **Key Directory:** All passwords are stored in the key directory (`.Crypter/files/keys/`). You can manage these keys manually, but they are essential for decryption.
- **Safety First:** Always test with a sample file before performing encryption on important files. Make sure to back up important data before encrypting it.

## Security Warning

Since this tool handles sensitive file encryption, it is essential to run it in a secure, isolated environment. The encryption and decryption processes can permanently alter the files, and losing the password can lead to irreversible data loss.

## Key Features & Functions

- **GenerateKey()**: Creates a new Fernet encryption key.
- **SaveKey()**: Saves the generated key to a password file.
- **LoadKey()**: Loads an existing key from a file.
- **Check()**: Verifies the existence of the key directory and creates it if necessary.
- **EncryptFilesInDir()**: Encrypts all files in a given directory.
- **DecryptFilesInDir()**: Decrypts all files in a given directory.
- **EncryptTree()**: Encrypts all files in a directory tree.
- **DecryptTree()**: Decrypts all files in a directory tree.
- **EncryptFile()**: Encrypts a specific file.
- **DecryptFile()**: Decrypts a specific file.
- **Clear()**: Clears the terminal screen after a delay.
- **Help()**: Displays the help text (currently a placeholder function).

## Conclusion

Crypto-Grapher is a simple yet powerful tool for file encryption and decryption. It is designed for use in secure, isolated environments and ensures that your files can be safely encrypted and decrypted with strong, password-based encryption. Remember to always back up your files and securely store your passwords to avoid any data loss.

For any questions or issues, refer to the help section or contact the tool's maintainer.

# Usage

## Running the Script

1. **Run the script**: Open the terminal and run the Python script using the following command:
   ```python crypter.py```

2. **Menu Options**: Once the script is running, the following options are available to choose from:

   - [1] Encrypt All Files in Directory Tree
   - [2] Decrypt All Files in Directory Tree
   - [3] Encrypt All Files in a Directory
   - [4] Decrypt All Files in a Directory
   - [5] Encrypt a Specific File
   - [6] Decrypt a Specific File
   - [7] Navigate to the Keys Directory
   - [8] List Directory Tree
   - [9] Help
   - [0] Exit

3. **Key Management**: When encrypting or decrypting files, you will be prompted for a password. This password is used to generate or retrieve an encryption key. The password is stored temporarily for the current session and is required for decryption.

4. **Directory Tree Encryption/Decryption**: The tool can process all files in a given directory, including all subdirectories. Make sure to input the full path correctly. If you're working in the current directory, use `.` as the path.

5. **Password/Key Generation**: If you need to generate a new password, simply provide a unique name when prompted. Each password corresponds to a unique key.

---

### Example Usage

1. **Encrypt all files in a directory tree**:
   - Select option [1] from the menu.
   - Enter the full path of the directory (e.g., `./` for the current directory).
   - Enter a secure password when prompted.
   - The tool will encrypt all files in the directory and its subdirectories.

2. **Decrypt all files in a directory tree**:
   - Select option [2] from the menu.
   - Enter the full path of the directory.
   - Enter the correct password to decrypt the files.

3. **Encrypt a specific file**:
   - Select option [5] from the menu.
   - Enter the full path to the file you want to encrypt.
   - Provide a secure password when prompted.

4. **Decrypt a specific file**:
   - Select option [6] from the menu.
   - Enter the full path to the file you want to decrypt.
   - Provide the correct password to decrypt the file.

---

### Important Notes

- **Key Management**: The password entered for encryption or decryption is used to generate or retrieve the corresponding encryption key. The password is only required once per session for each encryption/decryption task.

- **Directory Tree Operations**: When selecting options for encrypting or decrypting files in a directory tree, ensure that you enter the full path to the directory correctly. The tool will handle all subdirectories as well.

- **Irreversible Encryption**: If you lose the password, the encrypted files cannot be decrypted. Ensure you securely store the password.

- **One-Time Password (OTP)**: Each encryption operation uses a unique password (OTP). Ensure that you remember or securely store this password, as it will be required for decryption.

- **Testing**: Always test the encryption and decryption process with a sample file or directory to ensure it works as expected. Make backups of important files before proceeding with encryption.

---

### Example Commands for Common Use Cases

1. **Encrypting All Files in a Directory Tree**
- Run option [1] and input the full directory path.
- The tool will encrypt all files within the directory, including all subdirectories.

2. **Decrypting All Files in a Directory Tree**
- Run option [2] and provide the directory path.
- Enter the correct password to decrypt all the files within the directory.

3. **Encrypting a Specific File**
- Run option [5] and input the path to the specific file you wish to encrypt.
- Provide a secure password to encrypt that file.

4. **Decrypting a Specific File**
- Run option [6] and input the path to the file you wish to decrypt.
- Enter the correct password to decrypt the file.

5. **Navigating to the Keys Directory**
- Select option [7] to navigate to the directory where encryption keys are stored.
- This will help you manually manage keys if needed.

6. **Listing the Directory Tree**
- Use option [8] to view a listing of files in the current directory tree.
- This option can help you verify the files you wish to encrypt or decrypt.

---

### Safety Recommendations

- **Backup Your Files**: Always make sure to back up important files before encrypting them.
- **Password Security**: Never share your password or key file. Losing the password means losing access to the encrypted files.
- **Use Isolated Environments**: For added security, use the tool in a secure environment to protect your data.

---

# Author

*Created by Visvasrk and team*
*Human Nowhere*
*As a part of python file utility program*
*Date : 15 December 2024*


