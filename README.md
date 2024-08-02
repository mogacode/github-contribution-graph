# Random Commit Generator

This repository contains a Python script that generates a large number of random commits in a given Git repository. The script creates a specified number of commits, each with a random date within the past year and with random content. This can be useful for testing purposes or for generating a commit history in a new repository.

## Features

- Generates between 200 and 300 random commits.
- Each commit has a random date within the past year.
- Creates temporary files with random content for each commit.
- Commits are made using the specified date and time.
- Pushes the commits to the remote repository.

## Requirements

- Python 3.x
- `gitpython` library
- A valid Git repository

## Installation

1. Clone this repository or download the script.
2. Install the required dependencies using pip:
    ```sh
    pip install gitpython
    ```

## Usage

1. Modify the `repo_path` variable in the script to point to your local Git repository.

    ```python
    repo_path = r'C:\Users\namee\Downloads\test\test'  # Change to your repository path
    ```

2. Run the script:
    ```sh
    python create_many_commits.py
    ```

## Script Explanation

The `create_many_commits` function performs the following steps:

1. Checks if the provided repository path is valid.
2. Changes the working directory to the repository path.
3. Initializes the repository using `gitpython`.
4. Generates a random number of commits (between 200 and 300).
5. For each commit:
    - Generates a random date within the past year.
    - Creates a temporary file with random content.
    - Adds the file to the Git index.
    - Sets the author and committer dates.
    - Commits the changes.
    - Removes the temporary file.
6. Pushes the commits to the remote repository.
