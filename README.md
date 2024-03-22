
#  Data Scientist Salary Estimator Overview

* Developed a salary estimation tool with an average MAE of $11K for data scientists to facilitate 
  salary negotiation.
* Scraped over 1000 job descriptions from Glassdoor using Python and Selenium.
* Engineered features from job description text to quantify the value companies place on Python, 
  Excel, tableau, and Spark skills.
* Optimized Linear Regression, Lasso Regression, and Random Forest Regressor models using 
  GridsearchCV.
* Built a user-friendly API with Flask for client interaction and accessibility.


# Code and Resources Used
**Python Version**: 3.7
**Packages**: numpy, pandas, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
**For Web Framework Requirements**: pip install -r requirements.txt

## Web Scraping

Wrote a web scraper to scrape about 1000 job postings from glassdoor.com and collected the below-mentioned variables:

* Job Title
* Salary Estimate
* Rating
* Company
* Location
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

  ## Data Cleaning

Following data scraping, rigorous data preprocessing was essential to ensure suitability for our model. The subsequent alterations and variables generated include:

* Extracted numeric salary data and created separate columns for employer-provided salary and hourly wages.
* Removed rows with missing salary information to ensure data cleanliness.
* Parsed company ratings from the textual data and incorporated them into the dataset.
* Introduced a new column indicating the state where the company is located.
* Included a column to identify whether the job was at the company's headquarters.
* Transformed the founding date of companies into the age of the company for analysis.
* Generated binary columns to indicate the presence of specific skills  in job descriptions:
          * Python
          * SQL
          * tableau
          * spark
* Added columns for simplified job titles and seniority levels.
* Calculated and included the length of job descriptions in a separate column.

# Exploratary Data Analysis

I examined the distributions of the data and the frequency of values for different categorical variables. Here are some key points gathered from the pivot tables.

![image](https://github.com/thedv/ds_salary_proj/assets/86904885/38d2762e-ec10-4510-bd51-56d046a49ce4 )


![image](https://github.com/thedv/ds_salary_proj/assets/86904885/52d502d5-df76-4530-a9d5-8cb20875cff3 "Coorelation plot")


![image](https://github.com/thedv/ds_salary_proj/assets/86904885/586a45f1-a086-49b0-8d8f-c26b85e99987)


# Model Building


Initially, I encoded categorical variables into dummy variables and subsequently split the dataset into training and testing sets, allocating 20% for testing.

For model selection, I experimented with three different approaches and assessed their performance using Mean Absolute Error (MAE), a metric chosen due to its interpretability and robustness to outliers in this context.

The three models tested were:

**Multiple Linear Regression**: Served as the baseline model.
**Lasso Regression**: Considering the sparsity stemming from numerous categorical variables, I anticipated that a normalized regression approach like Lasso would yield favorable results.
**Random Forest**: Given the inherent sparsity in the data, Random Forest was deemed a suitable candidate for modeling.


# Model Performance

After training and testing all the models, the model that outperformed all the other models on the test and validation sets is Random Forest.

  * Random Forest: MAE = 5.91
  * Linear Regression: MAE = 19.15
  * Lasso Regression: MAE = 19.16

# Productionization

During this phase, I constructed a Flask API endpoint hosted on a local web server, following the guidance outlined in the  [TDS]([https://www.google.com](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2 ) tutorial. The API endpoint accepts requests containing a list of values extracted from a job listing and returns an estimated salary as output.


Note: This is an academic and learning purpose project and I would like to give credits to **Ken Jee** for his amazing content that helped me with this project.
