#!/usr/bin/env python
# coding: utf-8

# # PyCity Schools Analysis
# 
# - Your analysis here
#   
# ---

# ## District Summary

# In[ ]:


#(this was practice with tutor)
Df1 df2

df1  zipcode      df2   no.stu
abc  12345        abc   100
dff  56789        efg   50
efg  24680        hij   75

df3 (left) zipcode no.stu  
abc        12345   100
dff        56789   NA
efg        24680   50

df3 (inner) zipcode no.stu  
abc        12345   100
efg        24680   50

df3 (right) no.stu  zipcode
abc         100     12345
efg         50      24680
hij         75      NA









# In[1]:


# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[2]:


print(len(school_data_complete))


# In[3]:


#(practice with tutor)
school_data_complete2 = pd.merge(student_data, school_data, how="inner", on=["school_name", "school_name"])
school_data_complete2.head()


# In[4]:


print(len(school_data_complete2))


# In[7]:


# Calculate the total number of unique schools
# google count number of unique values in dataframe column
school_count = ['school_data_complete']. nunique()
school_count


# In[2]:


# Calculate the total number of unique schools
school_count = 
school_count


# In[70]:


# Calculate the total number of unique schools (My Code)
school_count = school_data_complete['school_name'].nunique()
print(school_count)


# In[3]:


# Calculate the total number of students
student_count = 
student_count


# In[71]:


# Calculate the total number of students (My code)
student_count = len(school_data_complete)
print(student_count)


# In[4]:


# Calculate the total budget
total_budget = 
total_budget


# In[72]:


# Calculate the total budget (My code)
total_budget = school_data_complete.groupby('school_name')['budget'].max().sum()
print(total_budget)


# In[5]:


# Calculate the average (mean) math score
average_math_score = 
average_math_score


# In[73]:


# Calculate the average (mean) math score (My code)
average_math_score = school_data_complete['math_score'].mean()
print(average_math_score)


# In[6]:


# Calculate the average (mean) reading score
average_reading_score = 
average_reading_score


# In[74]:


# Calculate the average (mean) reading score (My code)
average_reading_score = school_data_complete['reading_score'].mean()
print(average_reading_score)


# In[57]:


# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
(passing_math_count / 'student_count') * 100


# In[69]:


# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70) (My code)
student_count = len(school_data_complete)
passing_math = school_data_complete[school_data_complete['math_score'] >= 70]
passing_math_count = len(passing_math)
passing_percent = ((passing_math_count / student_count) * 100)
print(passing_percent)


# In[8]:


# Calculate the percentage of students who passed reading (hint: look at how the math percentage was calculated)  
passing_reading_count = 
passing_reading_percentage = 


# In[68]:


# Calculate the percentage of students who passed reading (hint: look at how the math percentage was calculated) (My code) 
student_count = len(school_data_complete)
passing_reading = school_data_complete[school_data_complete['reading_score'] >= 70]
passing_reading_count = len(passing_reading)
passing_percent = ((passing_reading_count / student_count) * 100)
print(passing_percent)


# In[9]:


# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = school_data_complete[(school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
overall_passing_rate


# In[75]:


# Use the following to calculate the percentage of students that passed math and reading (My code)
student_count = len(school_data_complete)
passing_math_reading = school_data_complete[(school_data_complete['math_score'] >= 70) & (school_data_complete['reading_score'] >= 70)]
passing_math_reading_count = len(passing_math_reading)
overall_passing_rate = (passing_math_reading_count / student_count) * 100
print(overall_passing_rate)


# In[10]:


# Create a high-level snapshot of the district's key metrics in a DataFrame
district_summary = 

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)

# Display the DataFrame
district_summary


# In[78]:


# Create a high-level snapshot of the district's key metrics in a DataFrame (My code)

#Key metric calculations
total_schools = school_count
total_students = student_count
total_budget = school_data_complete.groupby('school_name')['budget'].max().sum()
average_math_score = school_data_complete['math_score'].mean()
average_reading_score = school_data_complete['reading_score'].mean()
passing_math_percentage = (school_data_complete['math_score'] >= 70).mean() * 100
passing_reading_percentage = (school_data_complete['reading_score'] >= 70).mean() * 100
passing_math_reading_percentage = ((school_data_complete['math_score'] >= 70) & (school_data_complete['reading_score'] >= 70)).mean() * 100

district_summary = pd.DataFrame({
    "Total Schools": [total_schools],
    "Total Students": [total_students],
    "Total Budget": [total_budget],
    "Average Math Score": [average_math_score],
    "Average Reading Score": [average_reading_score],
    "% Passing Math": [passing_math_percentage],
    "% Passing Reading": [passing_reading_percentage],
    "% Overall Passing": [passing_math_reading_percentage]})

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)

# Display the DataFrame
print(district_summary)


# ## School Summary

# In[11]:


# Use the code provided to select all of the school types
school_types = 


# In[79]:


# Use the code provided to select all of the school types (My code)
school_types = school_data_complete['type'].unique()
print(school_types)


# In[12]:


# Calculate the total student count per school
per_school_counts = 


# In[80]:


# Calculate the total student count per school (My code)
per_school_counts = school_data_complete.groupby('school_name')['student_name'].count()
print(per_school_counts)


# In[13]:


# Calculate the total school budget and per capita spending per school
per_school_budget = 
per_school_capita = 


# In[85]:


# Calculate the total school budget and per capita spending per school (My Code)
per_school_budget = school_data_complete.groupby('school_name')['budget'].max()
print(per_school_budget)
per_school_capita = school_data_complete.groupby('school_name').agg({'budget': 'max', 'student_name': 'count'})
print(per_school_capita)


# In[14]:


# Calculate the average test scores per school
per_school_math = 
per_school_reading = 


# In[86]:


# Calculate the average test scores per school (My code)
per_school_math = school_data_complete.groupby('school_name').agg({'math_score': 'mean'})
per_school_reading = school_data_complete.groupby('school_name').agg({'reading_score': 'mean'})
print(per_school_math)
print(per_school_reading)


# In[15]:


# Calculate the number of students per school with math scores of 70 or higher
students_passing_math = 
school_students_passing_math = 


# In[91]:


# Calculate the number of students per school with math scores of 70 or higher (My code)
students_passing_math = school_data_complete[school_data_complete['math_score'] >= 70]
school_students_passing_math = students_passing_math.groupby('school_name')['student_name'].count()
print(school_students_passing_math)


# In[16]:


# Calculate the number of students per school with reading scores of 70 or higher
students_passing_reading = 
school_students_passing_reading = 


# In[90]:


# Calculate the number of students per school with reading scores of 70 or higher (My code)
students_passing_reading = school_data_complete[school_data_complete['reading_score'] >= 70]
school_students_passing_reading = students_passing_reading.groupby('school_name')['student_name'].count()
print(school_students_passing_reading)


# In[17]:


# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
students_passing_math_and_reading = school_data_complete[
    (school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)
]
school_students_passing_math_and_reading = students_passing_math_and_reading.groupby(["school_name"]).size()


# In[93]:


# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
students_passing_math_and_reading = school_data_complete[(school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)]
school_students_passing_math_and_reading = students_passing_math_and_reading.groupby(["school_name"]).size()
print(school_students_passing_math_and_reading)


# In[18]:


# Use the provided code to calculate the passing rates
per_school_passing_math = school_students_passing_math / per_school_counts * 100
per_school_passing_reading = school_students_passing_reading / per_school_counts * 100
overall_passing_rate = school_students_passing_math_and_reading / per_school_counts * 100


# In[99]:


# Use the provided code to calculate the passing rates
per_school_passing_math = school_students_passing_math / per_school_counts * 100
per_school_passing_reading = school_students_passing_reading / per_school_counts * 100
overall_passing_rate = school_students_passing_math_and_reading / per_school_counts * 100

print(per_school_passing_math)

print(per_school_passing_reading)

print(overall_passing_rate)


# In[19]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary = 

# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)

# Display the DataFrame
per_school_summary


# In[127]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above. (My code)
per_school_summary = school_data_complete.groupby('school_name').agg({
    'type': 'first',
    'budget': 'first',
    'student_name': 'count',
    'math_score': 'mean',
    'reading_score': 'mean'
})
# Calculate per capita spending
per_school_summary['Per Student Budget'] = per_school_summary['budget'] / per_school_summary['student_name']

# Calculate the percentage of students passing math, reading, and both
per_school_summary['% Passing Math'] = (school_data_complete[school_data_complete['math_score'] >= 70]
                                        .groupby('school_name')['student_name'].count() / per_school_summary['student_name']) * 100

per_school_summary['% Passing Reading'] = (school_data_complete[school_data_complete['reading_score'] >= 70]
                                           .groupby('school_name')['student_name'].count() / per_school_summary['student_name']) * 100

per_school_summary['% Overall Passing'] = (school_data_complete[(school_data_complete['math_score'] >= 70) &
                                                              (school_data_complete['reading_score'] >= 70)]
                                           .groupby('school_name')['student_name'].count() / per_school_summary['student_name']) * 100
# Formatting
per_school_summary['budget'] = per_school_summary['budget'].map("${:,.2f}".format)
per_school_summary['Per Student Budget'] = per_school_summary['Per Student Budget'].map("${:,.2f}".format)


# Display the DataFrame
print(per_school_summary)


# ## Highest-Performing Schools (by % Overall Passing)

# In[20]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
top_schools = 
top_schools.head(5)


# In[121]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows. (My code)
top_schools = per_school_summary.sort_values(by='% Overall Passing', ascending=False)
top_schools.head(5)


# ## Bottom Performing Schools (By % Overall Passing)

# In[21]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
bottom_schools = 
bottom_schools.head(5)


# In[122]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows. (My code)
bottom_schools = per_school_summary.sort_values(by='% Overall Passing', ascending=True)
bottom_schools.head(5)


# ## Math Scores by Grade

# In[22]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the `math_score` column for each.
ninth_grade_math_scores = 
tenth_grader_math_scores = 
eleventh_grader_math_scores = 
twelfth_grader_math_scores = 

# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade = 

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade


# In[123]:


# Use the code provided to separate the data by grade (My code)
ninth_graders = school_data_complete[school_data_complete["grade"] == "9th"]
tenth_graders = school_data_complete[school_data_complete["grade"] == "10th"]
eleventh_graders = school_data_complete[school_data_complete["grade"] == "11th"]
twelfth_graders = school_data_complete[school_data_complete["grade"] == "12th"]

# Group by `school_name` and take the mean of the `math_score` column for each grade
ninth_grade_math_scores = ninth_graders.groupby("school_name")["math_score"].mean()
tenth_grader_math_scores = tenth_graders.groupby("school_name")["math_score"].mean()
eleventh_grader_math_scores = eleventh_graders.groupby("school_name")["math_score"].mean()
twelfth_grader_math_scores = twelfth_graders.groupby("school_name")["math_score"].mean()

# Combine the math scores for each grade into a single DataFrame called `math_scores_by_grade`
math_scores_by_grade = pd.DataFrame({
    "9th": ninth_grade_math_scores,
    "10th": tenth_grader_math_scores,
    "11th": eleventh_grader_math_scores,
    "12th": twelfth_grader_math_scores
})

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade


# ## Reading Score by Grade 

# In[23]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the the `reading_score` column for each.
ninth_grade_reading_scores = 
tenth_grader_reading_scores = 
eleventh_grader_reading_scores = 
twelfth_grader_reading_scores = 

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = 

# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade


# In[124]:


# Use the code provided to separate the data by grade (My code)
ninth_graders = school_data_complete[school_data_complete["grade"] == "9th"]
tenth_graders = school_data_complete[school_data_complete["grade"] == "10th"]
eleventh_graders = school_data_complete[school_data_complete["grade"] == "11th"]
twelfth_graders = school_data_complete[school_data_complete["grade"] == "12th"]

# Group by `school_name` and take the mean of the `reading_score` column for each grade
ninth_grade_reading_scores = ninth_graders.groupby("school_name")["reading_score"].mean()
tenth_grader_reading_scores = tenth_graders.groupby("school_name")["reading_score"].mean()
eleventh_grader_reading_scores = eleventh_graders.groupby("school_name")["reading_score"].mean()
twelfth_grader_reading_scores = twelfth_graders.groupby("school_name")["reading_score"].mean()

# Combine the reading scores for each grade into a single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame({
    "9th": ninth_grade_reading_scores,
    "10th": tenth_grader_reading_scores,
    "11th": eleventh_grader_reading_scores,
    "12th": twelfth_grader_reading_scores
})

# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade


# ## Scores by School Spending

# In[24]:


# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[134]:


# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[25]:


# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()


# In[135]:


# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()


# In[26]:


# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = school_spending_df


# In[162]:


# Establish the bins (My code)
spending_bins = [0, 585, 630, 645, 680]
group_labels = ["$<$585", "$585-630", "$630-645", "$645-680"]
bins = spending_bins
labels = group_labels

# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()
school_spending_df["Per Student Budget"] = school_spending_df["Per Student Budget"].str.replace('$', '').str.replace(',', '')
school_spending_df["Per Student Budget"] = pd.to_numeric(school_spending_df["Per Student Budget"])

# Use pd.cut to categorize spending based on the bins and create a new column
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(school_spending_df["Per Student Budget"], bins=spending_bins, labels=group_labels)

# Display the DataFrame
print(school_spending_df)


# In[27]:


#  Calculate averages for the desired columns. 
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Overall Passing"].mean()


# In[168]:


#  Calculate averages for the desired columns. 
spending_math_scores = print(school_spending_df.groupby("Spending Ranges (Per Student)")["math_score"].mean())
spending_reading_scores = print(school_spending_df.groupby("Spending Ranges (Per Student)")["reading_score"].mean())
spending_passing_math = print(school_spending_df.groupby("Spending Ranges (Per Student)")["% Passing Math"].mean())
spending_passing_reading = print(school_spending_df.groupby("Spending Ranges (Per Student)")["% Passing Reading"].mean())
overall_passing_spending = print(school_spending_df.groupby("Spending Ranges (Per Student)")["% Overall Passing"].mean())


# In[28]:


# Assemble into DataFrame
spending_summary = 

# Display results
spending_summary


# In[173]:


# Assemble into DataFrame (My code)
spending_summary = pd.DataFrame({
    "Average Math Score": spending_math_scores,
    "Average Reading Score": spending_reading_scores,
    "% Passing Math": spending_passing_math,
    "% Passing Reading": spending_passing_reading,
    "% Overall Passing": overall_passing_spending
})

# Display results
spending_summary


# ## Scores by School Size

# In[174]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[30]:


# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

per_school_summary["School Size"] = 
per_school_summary


# In[175]:


# Define the bins and labels for school size categories (My code)
size_bins = [0, 1000, 2000, 5000]
size_labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Use pd.cut to categorize school size based on the "Total Students" column
per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"], bins=size_bins, labels=size_labels)

# Display the DataFrame
print(per_school_summary)


# In[31]:


# Calculate averages for the desired columns. 
size_math_scores = per_school_summary.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = per_school_summary.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = per_school_summary.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = per_school_summary.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = per_school_summary.groupby(["School Size"])["% Overall Passing"].mean()


# In[176]:


# Calculate averages for the desired columns. (My code)
size_math_scores = per_school_summary.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = per_school_summary.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = per_school_summary.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = per_school_summary.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = per_school_summary.groupby(["School Size"])["% Overall Passing"].mean()


# In[32]:


# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`
size_summary = 

# Display results
size_summary


# ## Scores by School Type

# In[33]:


# Group the per_school_summary DataFrame by "School Type" and average the results.
average_math_score_by_type = per_school_summary.groupby(["School Type"])["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby(["School Type"])["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby(["School Type"])["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby(["School Type"])["% Overall Passing"].mean()


# In[34]:


# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = 

# Display results
type_summary


# In[ ]:




