#!/usr/bin/env python
# coding: utf-8

# ## Exploratory_Data_Analysis

# In[4]:


Image("E:\DataScience\Data_Center\T_20_World_cup_data\ICC_Men's_T20_World_Cup_2021.png")


# In[1]:


pwd


# In[2]:


import os
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('darkgrid')
import plotly.express as px
import pandas as pd
import numpy as np
from scipy import signal

#to supress warning
import warnings
warnings.filterwarnings('ignore')


#to make shell more intractive
from IPython.display import display
from IPython.display import Image

# setting up the chart size and background
plt.rcParams['figure.figsize'] = (16, 8)
plt.style.use('fivethirtyeight')


# In[3]:


path ="E:\DataScience\Data_Center\T_20_World_cup_data"
dir_list = os.listdir(path)
print(dir_list)


# In[5]:


df =pd.read_csv("E:\DataScience\Data_Center\T_20_World_cup_data\kaggle_data.csv")


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.columns


# In[9]:


df.describe()


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[12]:


df.nunique(axis=0)


# In[13]:


A=df['team_1'].unique()
print(A)


# In[14]:


B =df['stage'].unique()
print(B)


# In[15]:


C=df['Winner_toss'].unique()
print(C)


# In[16]:


D=df['Toss_descision'].unique()
print(D)


# In[17]:


E=df['time'].unique()
print(E)


# In[18]:


F =df['venue'].unique()
print(F)


# In[19]:


G=df['avg_temperature'].unique()
print(G)


# In[20]:


I =df['best_bowler'].unique()
print(I)


# In[21]:


H =df['bowling_arm'].unique()
print(H)


# In[22]:


J =df['bowling_style'].unique()
print(J)


# In[23]:


K =df['most_individual_wickets'].unique()
print(K)


# In[24]:


H =df['best_batter_team'].unique()
print(H)


# In[25]:


I =df['Player_of_the_match'].unique()
print(I)


# In[26]:


#remnaming
df = df.rename(columns = {'Unnamed: 0' : 'Match Number'})
df.head()


# In[27]:


#index match
df = df.set_index('Match Number')
df.head()


# In[28]:


Time =df['time'].value_counts()


# In[29]:


Time


# In[30]:


type(Time)


# In[31]:


toss_list =df['Winner_toss'].tolist()
win_list=df['Winner'].tolist()
winner=0
looser=0
for i in range(len(toss_list)):
    if(toss_list[i] == win_list[i]):
        winner +=1
    else:
        looser +=1
        
        
print("Won Toss and Won Match:",winner)
print("Won Toss and Loose Match:",looser)


# In[32]:


#match won by each team
plt.figure(figsize = (8,6))
sns.countplot(df['time'], palette = 'Set1')
plt.title("Time Slot :Match")
plt.show()


# In[33]:


# Temprature range:
fig =px.pie(Time ,values =df['avg_temperature'].value_counts(),names=['30-Temp','33-Temp','34-Temp','29-Temp',
                                                                      '28-Temp','31-Temp','20-Temp','27-temp','26-Temp'],
            title=' Temparature Range Records while Match:')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
#temp in *c


# In[34]:


#match won by each team
sns.countplot(y='Winner',data=df)


# In[35]:


#count of venue
plt.figure(figsize = (8,6))
sns.countplot(df['venue'], palette = 'Set1')
plt.title("Venue for Tournament")
plt.show()


# In[36]:


#Man of MATCH
print("Player : No_of_times_player_of_match")
df['Player_of_the_match'].value_counts().nlargest(5)


# In[37]:


# correlation
plt.figure(figsize = (8,6))
sns.heatmap(df.corr(), annot = True, cmap = 'OrRd')
plt.title("Correlation")
plt.show()


# In[38]:


#colum name-update
df.target_achieved[df['target_achieved'] == 0] = 'Achieved'
df.target_achieved[df['target_achieved'] == 1] = 'Not Achieved'
df.head()


# In[39]:


plt.figure(figsize = (8,6))
sns.countplot(df['stage'], palette = 'Set1')
plt.title("Stage of Tournament")
plt.show()


# In[40]:


plt.figure(figsize = (8,6))
sns.countplot(y=df['best_batter_team'], palette = 'Set1')
plt.title("Best Batting Team")
plt.show()


# In[41]:


plt.figure(figsize = (8,6))
sns.countplot(y=df['best_bowler_country'], palette = 'Set1')
plt.title("Best Bolwing Team")
plt.show()


# In[42]:


print("Top 5 Batsman in T20-World-Cup-2021:")
df['best_batter'].value_counts().nlargest(5)


# In[43]:


print("Top 5 Bolwer in T20-World-Cup-2021:")
df['best_bowler'].value_counts().nlargest(5)


# In[44]:


print("Top 10 highest Score:")
df['target'].sort_values(ascending=False).nlargest(10)


# In[45]:


print("Least 10  Score:")
df['target'].sort_values(ascending=False).nsmallest(10)


# In[46]:


print("Top 10 high_indvidual_scores:")
df['high_indvidual_scores'].sort_values(ascending=False).nlargest(10)


# In[60]:


#by each team
plt.figure(figsize = (8,6))
sns.countplot(df['Toss_descision'], palette = 'Set1')
plt.title("Toss descision")
plt.show()


# In[ ]:





# In[47]:


#team 1 & target achievement
achieved_target_team1 = df.groupby(['team_1', 'target_achieved']).size().reset_index(name = 'Count')


# In[48]:


#visualize team 1
plt.figure(figsize = (10,6))
chart = sns.barplot(data =achieved_target_team1 , x = 'team_1', y ='Count', hue = 'target_achieved', palette = 'Set1')
chart.set_xticklabels(chart.get_xticklabels(), rotation = 35)
plt.title("Team 1 - Achievement")
plt.show()


# In[49]:


#team 2 & target achievement
achieved_target_team2 = df.groupby(['team_2', 'target_achieved']).size().reset_index(name = 'Count')


# In[50]:


#visualize team 2
plt.figure(figsize = (10,6))
chart = sns.barplot(data =achieved_target_team2 , x = 'team_2', y ='Count', hue = 'target_achieved', palette = 'Set1')
chart.set_xticklabels(chart.get_xticklabels(), rotation = 35)
plt.title("Team 2 - Achievement")
plt.show()


# In[51]:


Team =df.groupby(['team_1','team_2','Winner_toss','time','Toss_descision','venue','Player_of_the_match']).size()


# In[52]:


Team=Team.to_frame()


# In[53]:


Team


# In[54]:


type(Team)


# In[55]:


fig = px.sunburst(df, names=None, values=None, parents=None, path=['team_1','team_2','Toss_descision','Winner','venue'], 
                   color='team_2', color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, 
                  color_discrete_sequence=None, color_discrete_map={},
                  hover_data=['team_1','team_2','Toss_descision','Winner','venue'],
                 labels={}, title= "Team VS Team - Winner")
fig.show()


# In[56]:


Stage=df.groupby(['stage','team_1','team_2','Winner_toss','time','Toss_descision','venue']).size()


# In[57]:


Stage=Stage.to_frame()


# In[58]:


Stage


# In[59]:


fig = px.sunburst(df, names=None, values=None, parents=None, path=['stage','team_1','team_2','Winner_toss','time','Toss_descision','venue'], 
                   color='team_1', color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, 
                  color_discrete_sequence=None, color_discrete_map={},
                  hover_data=['stage','team_1','team_2','time','Toss_descision','venue'] ,
                 labels={'Stage','Team-A','Team-B','Time','Toss_descision','Venue'}, title= "Detailed_Analysis Chart")
fig.show()


# In[62]:


#
sns.pairplot(df,hue='team_1')


# In[ ]:


-----------------XXX-----------------
@copyright : Saurabh 29-nov

