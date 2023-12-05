from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def read_and_print_new_lines(file_path):
    # Check if a record file exists
    record_file_path = file_path + "_record.txt"
    if not os.path.exists(record_file_path):
        # If not, create one and record all lines as read
        with open(file_path, 'r') as file:
            lines = file.readlines()
            with open(record_file_path, 'w') as record_file:
                record_file.writelines(lines)
        return lines

    # Read the recorded lines
    with open(record_file_path, 'r') as record_file:
        recorded_lines = record_file.readlines()

    # Read all lines from the text file
    with open(file_path, 'r') as file:
        all_lines = file.readlines()

    # Identify new lines
    new_lines = [line.strip() for line in all_lines if line not in recorded_lines]

    # Update the record file with the latest lines
    with open(record_file_path, 'w') as record_file:
        record_file.writelines(all_lines)

    # Print the new lines in reverse order
    for line in reversed(new_lines):
        print(line)

    # Return the new lines in reverse order
    return list(reversed(new_lines))

@app.route('/get_new_lines', methods=['GET'])
def get_new_lines():
    file_path = '/Users/AdminBN/Documents/myVScode/911tasks/project3/activity_logs.txt'
    new_lines = read_and_print_new_lines(file_path)
    return jsonify({'new_lines': new_lines})

if __name__ == '__main__':
    app.run(debug=True)

    #this is a small change to test the Git
