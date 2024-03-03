from flask import Flask, request, render_template
import csv

app = Flask(__name__)

# Function to load the dataset
def load_dataset(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

# Updated path to your new dataset CSV file
dataset = load_dataset('topcomparisonsgpt4_outputV2.csv')

@app.route('/', methods=['GET'])
def index():
    return render_template('search2.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    # Accommodate for both GET and POST requests for the search query
    if request.method == 'POST':
        search_query = request.form['name'].lower().strip()
    else:
        search_query = request.args.get('name', '').lower().strip()

    filter_type = request.args.get('filter_type', 'highest')  # Default to showing highest matches

    # Filter results based on the search query
    name_matches = [row for row in dataset if search_query in row.get('Student_Name', '').lower() or search_query in row.get('Candidate_Name', '').lower()]

    if filter_type == 'highest' and name_matches:
        highest_score = max(name_matches, key=lambda x: int(x['Score'])).get('Score')
        results_to_show = [row for row in name_matches if row['Score'] == highest_score]
    else:
        results_to_show = name_matches

    total_matches = len(results_to_show)

    return render_template('results-active.html', results=results_to_show, total_matches=total_matches, search_query=search_query, filter_type=filter_type)

if __name__ == '__main__':
    app.run(debug=True)
