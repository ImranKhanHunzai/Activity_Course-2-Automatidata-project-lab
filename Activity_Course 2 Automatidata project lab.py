#!/usr/bin/env python
# coding: utf-8

# # **Automatidata project**
# **Course 2 - Get Started with Python**

# Welcome to the Automatidata Project!
# 
# You have just started as a data professional in a fictional data consulting firm, Automatidata. Their client, the New York City Taxi and Limousine Commission (New York City TLC), has hired the Automatidata team for its reputation in helping their clients develop data-based solutions.
# 
# The team is still in the early stages of the project. Previously, you were asked to complete a project proposal by your supervisor, DeShawn Washington. You have received notice that your project proposal has been approved and that New York City TLC has given the Automatidata team access to their data. To get clear insights, New York TLC's data must be analyzed, key variables identified, and the dataset ensured it is ready for analysis.
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # Course 2 End-of-course project: Inspect and analyze data
# 
# In this activity, you will examine data provided and prepare it for analysis.  This activity will help ensure the information is,
# 
# 1.   Ready to answer questions and yield insights
# 
# 2.   Ready for visualizations
# 
# 3.   Ready for future hypothesis testing and statistical methods
# <br/>    
# 
# **The purpose** of this project is to investigate and understand the data provided.
#   
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and inform team members of your findings. 
# <br/>  
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation 
# * Prepare to understand and organize the provided taxi cab dataset and information.
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities.
# 
# * Compile summary information about the data to inform next steps.
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into specific variables.
# 
# 
# <br/> 
# Follow the instructions and answer the following questions to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work. 
# 
# 

# # **Identify data types and relevant variables using Python**
# 

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## PACE: **Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided taxi cab information? 

# First I will understand the data, what changes (cleaning, sorting, filtering ) need to be done to the data. Then I will have a summery to get to the insights of the data. 

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: **Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Build dataframe**
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# Create a pandas dataframe for data learning, and future exploratory data analysis (EDA) and statistical activities.
# 
# **Code the following,**
# 
# *   import pandas as pd. pandas is used for buidling dataframes.
# 
# *   import numpy as np. numpy is imported with pandas
# 
# *   df = pd.read_csv('Datasets\NYC taxi data.csv')
# 
# **Note:** pair the data object name "df" with pandas functions to manipulate data, such as df.groupby().
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[1]:


#Import libraries and packages listed above
### YOUR CODE HERE ###
import pandas as pd
import numpy as np

# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")


# In[2]:


import pandas as pd
import numpy as np
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
df.head()


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by coding the following:
# 
# 1. df.head(10)
# 2. df.info()
# 3. df.describe()
# 
# Consider the following two questions:
# 
# **Question 1:** When reviewing the df.info() output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
# **Question 2:** When reviewing the df.describe() output, what do you notice about the distributions of each variable? Are there any questionable values?

# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# ==> ENTER YOUR RESPONSE TO QUESTIONS 1 & 2 HERE

# In[6]:


#==> ENTER YOUR CODE HERE
df.head(10)


# In[7]:


#==> ENTER YOUR CODE HERE
df.info()


# In[8]:


#==> ENTER YOUR CODE HERE
df.describe()


# ### **Task 2c. Understand the data - Investigate the variables**
# 
# Sort and interpret the data table for two variables:`trip_distance` and `total_amount`.
# 
# **Answer the following three questions:**
# 
# **Question 1:** Sort your first variable (`trip_distance`) from maximum to minimum value, do the values seem normal?
# 
# **Question 2:** Sort your by your second variable (`total_amount`), are any values unusual?
# 
# **Question 3:** Are the resulting rows similar for both sorts? Why or why not?

# In[9]:


df.sort_values(by='trip_distance', ascending= False)


# In[10]:


df.sort_values('total_amount', ascending = False)


# ==> ENTER YOUR RESPONSES TO QUESTION 1-3 HERE

# In[11]:


# ==> ENTER YOUR CODE HERE

# Sort the data by trip distance from maximum to minimum value
df.sort_values(by='trip_distance', ascending = False)


# In[12]:


#==> ENTER YOUR CODE HERE

# Sort the data by total amount and print the top 20 values
total_amount = df.sort_values(by='total_amount', ascending=False)['total_amount']
total_amount.head(n=20)


# In[13]:


#==> ENTER YOUR CODE HERE
sorted_data = df.sort_values(by='total_amount', ascending=False)
# Sort the data by total amount and print the bottom 20 values
sorted_data.tail(5)


# In[14]:


#==> ENTER YOUR CODE HERE

# How many of each payment type are represented in the data?
df_paymentType = pd.DataFrame(df['payment_type'])
df_paymentType.value_counts()


#df_paymentType.sort_values(by='payment_type', ascending=False)
# sorted_data = df.sort_values(by='total_amount', ascending=False)


# In[23]:


df_paymentType = pd.DataFrame(df['payment_type'])
df_paymentType.value_counts()


# In[15]:


#==> ENTER YOUR CODE HERE

# What is the average tip for trips paid for with credit card?
averageTip = df[df['payment_type']==1]['tip_amount'].mean()
print('Average tip by card', averageTip)

#==> ENTER YOUR CODE HERE
averageCashTip = df[df['payment_type']==2]['tip_amount'].mean()
print('Average tip by Cash', averageCashTip)

# What is the average tip for trips paid for with cash?


# In[24]:


average_tip = df[df['payment_type'] == 1 ]['tip_amount'].mean()
average_tip


# In[16]:


#==> ENTER YOUR CODE HERE
df['VendorID'].value_counts()

# How many times is each vendor ID represented in the data?


# In[26]:


df['VendorID'].value_counts()


# In[28]:


#==> ENTER YOUR CODE HERE
df.groupby(['VendorID']).mean(numeric_only=True)[['total_amount']]
# What is the mean total amount for each vendor?


# In[27]:


df.groupby(['VendorID']).mean(numeric_only = True)['total_amount']


# In[18]:


#==> ENTER YOUR CODE HERE

# Filter the data for credit card payments only
creditPayment = df[df['payment_type'] ==1]
#==> ENTER YOUR CODE HERE

# Filter the data for passenger count only
creditPayment['passenger_count'].value_counts()


# In[35]:


credit_payments = df[df['payment_type'] ==1]
credit_payments['passenger_count'].sum()


# In[36]:


#==> ENTER YOUR CODE HERE
creditPayment.groupby(['passenger_count']).mean(numeric_only=True)[['tip_amount']]
# Calculate the average tip amount for each passenger count (credit card payments only)


# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: **Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project. 
# 
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## PACE: **Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response.
# 

# ### **Given your efforts, what can you summarize for DeShawn and the data team?**
# 
# *Note for Learners: Your notebook should contain data that can address Luana's requests. Which two variables are most helpful for building a predictive model for the client: NYC TLC?*

# ==> ENTER YOUR RESPONSE HERE 
