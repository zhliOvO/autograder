# Autograder for C++

## Introduction
Designed to automate the process of grading C++ assignments. It compiles the submitted C++ code, runs it against predefined test cases, and checks the output against expected results.

## Features
- Compile C++ code submissions
- Run compiled programs with test cases
- Check coding style with `cpplint`
- Provide detailed output differences using `difflib`
- Log test results and resource usage

## Requirements
- Python3
- Flask
- g++

## Installation

Clone the repository to your local machine:

git clone https://github.com/zhliOvO/autograder.git
cd autograder

Set up a Python virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate  # On Unix or MacOS
venv\Scripts\Activate  # On Windows

Install the required Python packages:

pip install -r requirements.txt

## Usage

To start the autograder, run:

flask run

Navigate to `http://127.0.0.1:5000` in your web browser to access the web interface.

## Contributing

Written by Zhuoheng Li. Thanks to Chatgpt for helping me debug.

## Contact

zhlii@umich.edu
