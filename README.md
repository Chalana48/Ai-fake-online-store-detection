AI-Powered Fake Online Store Detection System

IT41043 — Intelligent Systems

Research Title:
AI-Powered Fake Online Store Detection System Using Machine Learning and Website Trust Indicators

Student: L. C. Isuranga Silva
Student ID: ITBIN-2313-0109
Partner: H. W. Thilina Dilshan Hettiarachchi
Academic Year: 2026

1. Project Overview

Online shopping through websites and social-media platforms has become increasingly popular. However, the growth of social commerce has also created opportunities for fraudulent online stores.

Fake online stores may advertise products at unusually low prices, collect payments from customers, and then fail to deliver the promised products or provide products that do not match the advertisements.

This research proposes a machine learning-based system for detecting fake online stores by combining traditional website trust indicators with online-shopping and social-commerce-related features.

The system focuses particularly on online stores operating through websites and social-media platforms in Sri Lanka and the wider South Asian context.


2. Research Question

> Does a machine learning model that combines website trust indicators and social media-related features achieve higher fake online store detection accuracy than traditional URL-based phishing detection methods?

The research will compare a URL-based baseline with a proposed model that combines URL, website-trust, shopping-behaviour, review and social-commerce features.

3. Research Objectives

Main Objective

To develop and evaluate a machine learning-based approach for detecting fake online stores using website trust indicators and social-commerce features.

Specific Objectives

1. Collect and curate a dataset of legitimate and fake online stores.
2. Identify relevant website trust and social-commerce features.
3. Preprocess and transform the collected data into machine-learning-ready features.
4. Develop a URL-only Logistic Regression baseline.
5. Develop a Random Forest model using the combined feature set.
6. Compare the proposed model with the baseline using appropriate evaluation metrics.
7. Analyse the contribution of different feature groups through feature importance and ablation analysis.

4. Dataset Plan

The proposed dataset target is approximately 1,200 online store records:

* 600 legitimate stores
* 600 fake stores

The final numbers will be updated after the actual data collection process.

Data Sources

The research will use publicly accessible information from:

* Online store websites
* Public social-commerce profiles
* Publicly available domain information
* Publicly available scam/fraud reports and warnings

Private messages, private accounts and restricted content will not be collected.

Feature Groups

The planned feature groups include:

URL and Domain Trust

* URL length
* Special-character count
* Subdomain count
* Domain age where available
* HTTPS availability

Website Trust

* Contact information clarity
* Refund/return policy
* Delivery policy
* Business information
* Payment-method category

Shopping Behaviour

* Suspicious discount indicators
* Product-price consistency
* Urgency-related indicators

Review Signals

* Review count
* Rating distribution
* Review consistency
* Repeated-text indicators
* Review completeness

Social-Commerce Signals

* Public follower range
* Posting frequency
* Public page age where available
* Engagement-rate aggregates
* Store identity consistency


## 5. Data Annotation

Each candidate store will be classified as:

* `fake`
* `legitimate`
* `uncertain`

Two annotators will independently evaluate the records using a predefined annotation procedure.

Evidence considered may include:

* Public scam reports
* Store identity consistency
* Delivery and return information
* Payment-risk indicators
* Domain and website information
* Independent supporting evidence

Cohen's kappa will be used to measure inter-annotator agreement.

Unresolved uncertain cases will not be forced into either class.


6. Data Preprocessing

The preprocessing stage will include:

1. URL normalisation
2. Duplicate-store removal
3. Missing-value handling
4. Numerical feature preparation
5. Categorical feature encoding
6. Feature transformation
7. Data leakage prevention

Preprocessing operations such as imputation, scaling, feature selection and model tuning will be performed using training data within the cross-validation process where appropriate.

7. Proposed Model

The proposed classifier is a Random Forest model.

The model will use a combined feature vector containing:

```text
URL/Domain Features
        +
Website Trust Features
        +
Shopping Behaviour Features
        +
Review Features
        +
Social-Commerce Features
        ↓
   Feature Fusion
        ↓
   Random Forest
        ↓
Fake / Legitimate
```

Random Forest was selected because the proposed dataset contains a mixture of numerical, categorical and binary indicators and may contain non-linear relationships between different trust and fraud-related features.

8. Baseline Model

The baseline model is URL-only Logistic Regression.

The baseline will use traditional URL/domain features such as:

* URL length
* Number of dots
* Number of hyphens
* Number of subdirectories
* Special-character count
* Subdomain count
* HTTPS indicator
* Domain-age availability
* IP-address-style host indicator

The baseline will use the same dataset, train/test organisation, cross-validation folds and evaluation metrics as the proposed Random Forest model.

This provides a fair comparison between traditional URL-based detection and the proposed hybrid feature approach.


9. Experimental Design

Dataset Split

The planned evaluation structure is:

```text
Complete Dataset
       │
       ├── 80% Development Set
       │       │
       │       └── Stratified 5-Fold Cross-Validation
       │
       └── 20% Untouched Test Set
```

The same folds and evaluation conditions will be used for both the baseline and proposed model.


10. Evaluation Metrics

The following metrics will be reported:

| Metric    | Purpose                                                             |
| --------- | ------------------------------------------------------------------- |
| Accuracy  | Overall classification performance                                  |
| Precision | Correctness of fake-store predictions                               |
| Recall    | Ability to identify fake stores                                     |
| F1-score  | Balance between precision and recall                                |
| ROC-AUC   | Overall classification discrimination                               |
| PR-AUC    | Additional measure if the final dataset is substantially imbalanced |

The primary threshold-based metric will be F1-score.


11. Statistical Analysis

The baseline and proposed model will be evaluated on the same cross-validation folds.

A Wilcoxon signed-rank test will be used to compare paired fold-level performance.

The significance level will be:

```text
α = 0.05
```

Where feasible, bootstrap confidence intervals will also be reported.

The study will consider both statistical significance and practical improvement in metrics such as F1-score and ROC-AUC.

12. Error Analysis

The research will include:

* Confusion matrices
* False-positive analysis
* False-negative analysis
* Feature-importance analysis
* Feature-group comparison

An ablation analysis will compare:

```text
Model 1: URL-only
Model 2: URL + Website Trust
Model 3: URL + Website Trust + Social-Commerce
```

This will help determine whether the additional feature groups improve fake online store detection.

13. System Architecture

The system follows this high-level workflow:

```text
Raw Data Sources
       ↓
Data Curation
       ↓
Preprocessing
       ↓
Feature Extraction
       ↓
Feature Fusion
       ↓
Random Forest Classifier
       ↓
Prediction
       ↓
Fake / Legitimate
```

The repository contains the vector system architecture diagram in:

```text
docs/system_architecture.svg
```

---

14. Project Structure

```text
ai-fake-online-store-detection/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── system_architecture.svg
│
├── notebooks/
│   └── 01_data_audit.ipynb
│
├── src/
│   ├── config.py
│   └── preprocess.py
│
├── requirements.txt
│
└── README.md
```

15. Ethical Considerations

This project will use publicly accessible store-level information.

The research will:

* Avoid private social-media content.
* Avoid private messages.
* Avoid collecting personal identifiers where possible.
* Not bypass authentication or access controls.
* Not bypass CAPTCHAs.
* Avoid exposing individual alleged scammers.
* Store only features necessary for the research.
* Consider geographic and platform bias.

A classification of a store as `fake` is treated as a research label and not as a legal determination.


16. Current Project Status

Milestone 1

* Research topic selected
* Research gap identified
* Research question defined
* Scope defined
* Initial bibliography prepared

Milestone 2

* Dataset methodology defined
* Feature groups identified
* Annotation process defined
* Ethical considerations defined
* Preprocessing methodology defined
* System architecture designed
* Baseline defined
* Evaluation strategy defined
* GitHub project structure prepared

Future Work

* Collect and curate the dataset
* Complete annotation
* Implement preprocessing
* Train baseline model
* Train Random Forest model
* Perform cross-validation
* Conduct statistical analysis
* Perform feature-importance and ablation analysis
* Analyse and report experimental results

17. Technologies

The planned implementation will use Python and common machine-learning/data-processing libraries.

Main technologies include:

* Python
* Pandas
* NumPy
* Scikit-learn
* SciPy
* Matplotlib
* Jupyter Notebook
* Git
* GitHub

18. Installation

Clone the repository:

```bash
git clone https://github.com/Chalana48/Ai-fake-online-store-detection.git
```

Move into the project directory:

```bash
cd ai-fake-online-store-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

19. Data Preprocessing

After placing the approved dataset in:

```text
data/raw/store_dataset.csv
```

run:

```bash
python src/preprocess.py
```

The processed dataset will be generated in:

```text
data/processed/model_ready.csv
```

Do not upload private information, credentials, API keys or restricted/raw personal data to the public repository.

20. Research Scope

Included

* Fake online store detection
* Website trust indicators
* URL/domain features
* Social-commerce features
* Review-related indicators
* Machine learning classification
* Model comparison
* Feature evaluation

Out of Scope

* Real-time production deployment
* Mobile application development
* Multi-language support
* Legal investigation of cybercriminals
* Banking-system integration
* Detection of all forms of online fraud outside e-commerce scams

21. Expected Contribution

The research aims to investigate whether combining traditional website trust indicators with social-commerce and online-shopping-related features can improve fake online store detection compared with URL-only detection.

The study will also investigate which feature groups contribute most strongly to classification performance.

22. Academic Project

This repository is developed as part of:

IT41043 — Intelligent Systems
Horizon Campus — Faculty of Information Technology
Academic Year 2026

Research project:
AI-Powered Fake Online Store Detection System Using Machine Learning and Website Trust Indicators
