# riPrint Graduate Project

Welcome to the `riPrint` graduate project. This project is aimed at creating a pen testing software around printers.

## Code Conventions

- **Class Naming**: We follow the PascalCase naming convention for classes. For instance, `PrintManager`.
- **Method Naming**: Methods should be named in camelCase. For example, `printDocument()`.
- **Variable Naming**: Variables should be named in camelCase. For example, `totalItemCount`.

## Modularity

Modularity is a fundamental software design principle that promotes the development of code in a way that makes it more maintainable, understandable, and extensible. It involves breaking down a complex system into smaller, independent, and reusable modules or components. 

### Waterfall example

```
# Waterfall Version

# Input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculation
area = length * width

# Output
print(f"The area of the rectangle is: {area}")

```

### Modular example
```
# Modular Version

# Function for input
def get_rectangle_dimensions():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length, width

# Function for calculation
def calculate_rectangle_area(length, width):
    return length * width

# Function for output
def display_area(area):
    print(f"The area of the rectangle is: {area}")

# Main program
if __name__ == "__main__":
    # Input
    length, width = get_rectangle_dimensions()
    
    # Calculation
    area = calculate_rectangle_area(length, width)
    
    # Output
    display_area(area)

```

## Data Structure

Please do not handle unnessicary logic inside the `main.py` file. The logic should all be handled in the `utils` folder.

## Setting Up Development Environment

### Python Virtual Environment

#### PowerShell (Windows)

```powershell
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate

Once activated, you can install the required packages using 'pip install -r requirements.txt'.
```

## Git Commands

Here are some basic git commands you should be familiar with:

1. Clone the repository: git clone <repository-url>
2. Create a new branch: git checkout -b <branch-name>
3. Add changes: git add .
4. Commit changes: git commit -m "Commit message"
5. Push changes to the repository: git push origin <branch-name>

Here is also how to authenticate yourself in the CLI

1. git config --global user.email "you@example.com"
2. git config --global user.name "yourName"


## Pull Requests (PR)

When you're ready to merge your changes into the main branch:

    1. Push your branch to the repository.
    2. On the repository's GitHub page, click on 'New Pull Request'.
    3. Select your branch from the dropdown.
    4. Add a meaningful title and description.
    5. Submit the PR and wait for reviews.

Ensure to resolve any feedback/comments on your PR before it gets merged!

## Network Packet Capture Library for Windows

For network packet capture and transmission capabilities, this project relies on the Npcap library. Ensure you have Npcap installed on your system to utilize network-related functionalities.

## Download and install Npcap

    1. Visit the [download page](https://npcap.com/#download)
    2. download the most recent version for your machine
    3. Walk through the installer and it should be good!

## Nmap system download

Install namp for system so python-nmap libray can be used

## Download and install Nmap

    1. Visit the [download page](https://nmap.org/download.html#windows)
    2. download the most recent version for your machine
    3. Walk through the installer and it should be good!


## Questions

Please reach out to Ethan Gormley (The 219 number) or eagormle@iu.edu
