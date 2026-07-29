from flask import Flask, jsonify

app = Flask(__name__)

# In-memory vote storage
votes = {
    "Rahul": 0,
    "Ram": 0,
    "Shyam": 0
}

@app.route("/")
def home():
    return """
    <h2>Welcome to the Voting Application</h2>
    <p>Available candidates:</p>
    <ul>
        <li>Rahul</li>
        <li>Ram</li>
        <li>Shyam</li>
    </ul>
    <p>Vote using: /vote/&lt;candidate&gt;</p>
    <p>View results using: /results</p>
    """

@app.route("/vote/<candidate>")
def vote(candidate):
    candidate = candidate.title()

    if candidate in votes:
        votes[candidate] += 1
        return f"Vote recorded for {candidate}!"
    else:
        return "Candidate not found!", 404

@app.route("/results")
def results():
    return jsonify(votes)

if __name__ == "__main__":
    app.run(debug=True)