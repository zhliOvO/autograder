import subprocess
import os
import difflib
import logging
import resource

# Paths for test cases and expected outputs are still needed
test_cases_directory = 'test_cases/'  
output_directory = 'expected_outputs/'  
executable = 'program'    
source_file_name = 'uploaded_program.cpp'  # This will be the name of the compiled source file

logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compile_and_run(source_filepath):
    results = []
    log = "Compilation started...\n"
    try:
        subprocess.run(['g++', source_filepath, '-o', executable], check=True)
        log += "Compilation successful.\n"
        results = run_test_cases()
    except subprocess.CalledProcessError as e:
        log += f"Compilation failed: {e}\n"
    return results, log

def run_test_cases():
    test_files = os.listdir(test_cases_directory)
    results = []

    for test in sorted(test_files):
        test_input_path = os.path.join(test_cases_directory, test)
        expected_output_path = os.path.join(output_directory, test)

        with open(test_input_path, 'r') as test_input, open(expected_output_path, 'r') as expected_output:
            proc = subprocess.run([f'./{executable}'], stdin=test_input, text=True, capture_output=True, timeout=2)
            output = proc.stdout
            expected = expected_output.read()

            result = {
                'test_case': test,
                'status': 'Passed' if output.strip() == expected.strip() else 'Failed',
                'output': output.strip(),
                'expected_output': expected.strip(),
                'diff': '\n'.join(difflib.unified_diff(
                    expected.strip().splitlines(),
                    output.strip().splitlines(),
                    fromfile='Expected output',
                    tofile='Your output',
                    lineterm=''
                ))
            }
            results.append(result)
    
    return results

# This is a placeholder for where you would implement code style checking
# def check_code_style(source_filepath):
#     pass
