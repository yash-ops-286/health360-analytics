# Health360: Comprehensive Healthcare Risk & Disease Analysis

## Project Overview
Health360 is an interactive healthcare analytics platform designed to uncover patterns across demographic profiles, lifestyle habits, and clinical indicators. The solution equips healthcare providers and public health researchers with visual intelligence to identify high-risk cohorts, optimize preventive intervention strategies, and monitor patient health trends.

---

## Technical Architecture & Pipeline
1. **Data Ingestion & Cleaning**: Extraction and ingestion of structured patient health metrics (Demographics, BMI, Blood Pressure, Lifestyle factors).
2. **Feature Engineering & Calculations**: Created clinical calculated fields in Tableau Desktop (BMI Category classification, Age Group segmentation, and aggregation measures).
3. **Interactive Dashboards & Stories**: 
   - **Scenario 1 & 3**: Heatmap analysis of patient counts across Age Groups vs. BMI Categories.
   - **Scenario 2**: Comparative bar visualizations evaluating lifestyle habits (Alcohol consumption, Chest Pain) against Systolic Blood Pressure.
   - **Executive Story**: Multi-point clinical narrative highlighting key patient summary metrics and risk distribution patterns.
4. **Web Integration**: Published to Tableau Public and seamlessly embedded into a Python Flask web portal using the Tableau JavaScript API.

---

## Technical Stack
- **Data Analytics & Visualisation**: Tableau Public / Tableau Desktop
- **Web Backend**: Python 3, Flask
- **Web Frontend**: HTML5, Modern CSS3, Tableau Embedding API v3
- **Deployment & Source Control**: Git, GitHub

---

## Local Setup & Execution Guide

### Prerequisites
- Python 3.10+
- Tableau Desktop Public Edition

### Installation Steps
1. Clone this repository:
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd health360-flask

   ## Live Links & Deliverables
- **Tableau Public Story**: [Health360 Executive Story](https://public.tableau.com/views/Health360ComprehensiveHealthcareRiskAnalysis_17932108388850/Health360ExecutiveStory)
- **GitHub Repository**: https://github.com/yash-ops-286/health360-analytics
- **Author**: Yash Kumar