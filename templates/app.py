from flask import Flask, render_template  # type: ignore[import-not-found]

app = Flask(__name__)

@app.route('/')
def home():
    tableau_url = "https://public.tableau.com/views/Health360ComprehensiveHealthcareRiskAnalysis_17932108388850/Health360ExecutiveStory"
    return render_template('index.html', tableau_url=tableau_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)