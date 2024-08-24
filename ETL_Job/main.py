import pandas as pd
import pycountry_convert as pc

# Step 1: Load the Data
survey_data = pd.read_csv("survey_results_public.csv")
schema_data = pd.read_csv('survey_results_schema.csv')

# Step 2: Average Age When Developers First Coded
survey_data['Age1stCode'] = pd.to_numeric(survey_data['Age1stCode'], errors='coerce')
average_age_first_code = survey_data['Age1stCode'].mean()
print(f"Average age when developers wrote their first line of code: {average_age_first_code:.2f}")

# Step 3: Percentage of Developers Who Knew Python by Country
python_devs = survey_data[survey_data['LanguageWorkedWith'].str.contains('Python', na=False)]
country_counts = survey_data['Country'].value_counts()
python_country_counts = python_devs['Country'].value_counts()
python_percentage_by_country = (python_country_counts / country_counts) * 100
print("\nPercentage of developers who knew Python by country:")
print(python_percentage_by_country)

# Step 4: Average Salary by Continent
def get_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        return continent_code
    except:
        return None

survey_data['Continent'] = survey_data['Country'].apply(get_continent)
average_salary_by_continent = survey_data.groupby('Continent')['ConvertedComp'].mean()
print("\nAverage salary by continent:")
print(average_salary_by_continent)

# Step 5: Most Desired Programming Language for 2020
desired_languages = survey_data['LanguageDesireNextYear'].str.split(';').explode().value_counts()
most_desired_language = desired_languages.idxmax()
print(f"\nMost desired programming language for 2020: {most_desired_language}")

# Step 6: Report for Hobby Coding by Gender and Continent
def categorize_gender(gender):
    if pd.isna(gender):
        return 'OTHERS'
    gender = gender.lower()
    if 'man' in gender:
        return 'MAN'
    elif 'woman' in gender:
        return 'WOMAN'
    else:
        return 'OTHERS'

survey_data['GenderCategory'] = survey_data['Gender'].apply(categorize_gender)
hobby_report = survey_data.groupby(['Continent', 'GenderCategory'])['Hobbyist'].value_counts(normalize=True).unstack().fillna(0)
print("\nReport for coding as a hobby by gender and continent:")
print(hobby_report)

# Step 7: Report for Job and Career Satisfaction by Gender and Continent

# Convert 'JobSat' and 'CareerSat' columns to numeric, forcing errors to NaN
survey_data['JobSat'] = pd.to_numeric(survey_data['JobSat'], errors='coerce')
survey_data['CareerSat'] = pd.to_numeric(survey_data['CareerSat'], errors='coerce')

satisfaction_report = survey_data.groupby(['Continent', 'GenderCategory'])[['JobSat', 'CareerSat']].mean()
print("\nReport for job and career satisfaction by gender and continent:")
print(satisfaction_report)
