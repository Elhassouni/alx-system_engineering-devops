# Uploadine Screenshots to Remote Server using SFTP

**Brief Overview of SFTP:**

SFTP (SSH File Transfer Protocol) is a secure file transfer protocol that enables you to transfer files securely over a network. It uses SSH (Secure Shell) for authentication and encryption, providing a secure way to transfer files between hosts.

**Instructions:**

Here are the steps I done to upload screenshots to a remote server using SFTP:

1. **Connect with SFTP**: Use the SFTP command to establish a connection to the remote server and enter the password when prompted.

2. **Navigate to Directory**: Once connected, navigate to the directory on the remote server where you want to upload the screenshots.

3. **List Local Files**: Use the `lls` command to list the files and directories on your local machine. Ensure that you are in the correct directory containing the screenshots you want to upload.

4. **Upload Screenshots**: Use the `put` command to upload the screenshots from your local machine to the remote server. Navigate to the directory containing the screenshots on your local machine, then use the `put` command followed by the path to the directory containing the screenshots. Press Enter to upload the screenshots to the remote server.

5. **Confirmation**: Once the upload is complete, you should see a confirmation message indicating that the files were successfully transferred.

That's it! You have successfully uploaded screenshots to the remote server using SFTP.

