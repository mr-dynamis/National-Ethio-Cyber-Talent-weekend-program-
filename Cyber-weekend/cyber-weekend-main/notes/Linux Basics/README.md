# 1. Linux User Management
This is about managing users in a Linux system.
Key points:
User vs Root (Superuser)
   - Normal user: limited permissions
   - Root user: full control of the   

# systemSuperUser DO (sudo)
- Allows a normal user to run commands as rootsudo apt update
-       sudo apt update
  # 2. Package Installation in Linux
This is how you install software using package managers.

  Common package managers:
- APT (used in Ubuntu/Debian)
-       sudo apt install package_name
-   Pacman (used in Arch Linux)
-      sudo pacman -S package_name
  #  3. Script Installation
- Scripts automate tasks.
-       nano script.sh
-      chmod +x script.sh
-     ./script.sh
-  A script is a file that contains a list of commands.
#  5. Shell
- A shell is a program that lets you interact with Linux.
- A shell is a program that acts as a bridge between you (the user) and the Linux operating system (kernel).
# Types of shell:
- Bash (most common)(Bourne Again Shell)
- Zsh (Z Shell)
- Sh (Bourne Shell)
-      User → Shell → Kernel → Hardware 
What happens:
- Shell reads the command
- Shell understands it
- Shell asks the OS to list files
- Output is shown to you
#  5.1 Shell Operators
-  Shell operators help you combine commands and control how they run.
 1. Pipe Operator (|) : Takes output of one command → sends it as input to another
-      ls | grep file
 2.  OR Operator (||) : Runs second command only if first fails
-      mkdir test || echo "failed"
 3. AND Operator (&&) : Runs next command only if first succeeds
 -     mkdir test && cd test
 4. Redirection Operators (>, >>, <)
    - Output Redirection (>)
      - Saves output to a file
      -      echo "Hello" > file.txt
    - Append (>>)
      - Adds to file
      -      echo "Hi" >> file.txt
    - Input Redirection (<)
       - Takes input from a file
       -      cat < file.txt
5. Semicolon (;)
   - Runs commands one after another (no condition)
   -      mkdir test; cd test; touch file.txt
