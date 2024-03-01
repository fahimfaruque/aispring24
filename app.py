from flask import Flask, request, render_template
import csv

app = Flask(__name__)

# Function to load the dataset
def load_dataset(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

# path to your dataset CSV file
dataset = load_dataset('dataset_with_html_rationale.csv')

# Route for the search form
@app.route('/', methods=['GET'])
def index():
    return render_template('search.html')

# Route to handle search requests
@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['name'].lower().strip()
    # Filter results based on the search query
    results = [row for row in dataset if search_query in row['Student_Name'].lower() or search_query in row['Candidate_Name'].lower()]

    # Extract unique scores from the filtered results
    unique_scores = sorted({int(row['Score']) for row in results}, reverse=True)

    # Pass both the results and the unique scores for filtering to the template
    return render_template('results.html', results=results, unique_scores=unique_scores)

if __name__ == '__main__':
    app.run(debug=True)
