from flask import Flask, request, render_template
import csv

app = Flask(__name__)

# Function to load the dataset
def load_dataset(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

# Updated path to your new dataset CSV file
dataset = load_dataset('topcomparisonsgpt4_outputV2.csv')

# Route for the search form
@app.route('/', methods=['GET'])
def index():
    return render_template('search2.html')

# Route to handle search requests
@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['name'].lower().strip()
    results = [row for row in dataset if search_query in row.get('Student_Name', '').lower() or search_query in row.get('Candidate_Name', '').lower()]
    filtered_results = [{
        'Student_Name': row['Student_Name'],
        'Student_Email': row['Student_Email'],
        'Student_LinkedIn': row['Student_LinkedIn'],
        'Candidate_Name': row['Candidate_Name'],
        'Candidate_Email': row['Candidate_Email'],
        'Candidate_LinkedIn': row['Candidate_LinkedIn'],
        'Rationale': row['Rationale'],
        'Score': row['score']  # Ensure this matches the field name in your CSV
    } for row in results]

    unique_scores = sorted({int(row['Score']) for row in filtered_results})
    
    return render_template('results2.html', results=filtered_results, unique_scores=unique_scores)
if __name__ == '__main__':
    app.run(debug=True)
