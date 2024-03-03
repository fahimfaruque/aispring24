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
# @app.route('/search', methods=['POST'])
# def search():
#     search_query = request.form['name'].lower().strip()
#     results = [row for row in dataset if search_query in row.get('Student_Name', '').lower() or search_query in row.get('Candidate_Name', '').lower()]
#     filtered_results = [{
#         'Student_Name': row['Student_Name'],
#         'Student_Email': row['Student_Email'],
#         'Student_LinkedIn': row['Student_LinkedIn'],
#         'Candidate_Name': row['Candidate_Name'],
#         'Candidate_Email': row['Candidate_Email'],
#         'Candidate_LinkedIn': row['Candidate_LinkedIn'],
#         'Rationale': row['Rationale'],
#         'score': row['score']  # Ensure this matches the field name in your CSV
#     } for row in results]

#     unique_scores = sorted({int(row['score']) for row in filtered_results})
    
#     return render_template('results-active.html', results=filtered_results, unique_scores=unique_scores)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_query = request.form['name'].lower().strip() if request.method == 'POST' else ''
    score_filter = request.args.get('score_filter')

    # Convert unique scores to integers for sorting, ensuring only valid strings are converted
    unique_scores = sorted({row['Score'] for row in dataset if row['Score'].isdigit()}, key=lambda x: int(x), reverse=True)

    # If no score_filter is provided, default to the highest score
    if not score_filter or not score_filter.isdigit():
        score_filter = unique_scores[0] if unique_scores else None
    else:
        score_filter = score_filter

    # Filter dataset based on search query
    results = [row for row in dataset if search_query in row.get('Student_Name', '').lower() or search_query in row.get('Candidate_Name', '').lower()]
    
    # Further filter results based on score, converting scores to integers for comparison
    if score_filter:
        results = [row for row in results if row.get('Score').isdigit() and int(row.get('Score')) == int(score_filter)]

    return render_template('results-active.html', results=results, unique_scores=unique_scores, current_filter=score_filter)





if __name__ == '__main__':
    app.run(debug=True)
