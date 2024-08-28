from flask import Flask, render_template, request, jsonify
import os
import git
from datetime import datetime

app = Flask(__name__)

# Create a directory to save the notes if it doesn't exist
notes_directory = "Notes"
os.makedirs(notes_directory, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_note():
    data = request.json
    filename = data['filename'] + '.txt'
    file_path = os.path.join(notes_directory, filename)
    
    # Save the note content to the specified file
    with open(file_path, 'a') as file:
        file.write(data['content'])
    
    # Commit changes using git
    commit_changes(filename)  # Pass only the filename
    
    return jsonify({"status": "success"})

def commit_changes(filename):
    repo = git.Repo.init(notes_directory)
    
    # Add the file to the staging area relative to the notes directory
    repo.index.add([filename])
    
    # Commit the changes
    commit_message = f"Auto-commit: {filename} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    repo.index.commit(commit_message)

if __name__ == '__main__':
    app.run(debug=True)
