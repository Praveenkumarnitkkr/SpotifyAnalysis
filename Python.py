
 #Importing Libraries that are used further in the Project...

from __future__ import annotations
from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('tracks.csv')   # Reading our csv file

df.head()

#null values
pd.isnull(df).sum()

#Total Number of columns and Rows
df.shape

#Info 
df.info()

# 10 Least popular songs on spotify

least=df.sort_values('popularity',ascending=True).head(10)

# 10 most popular songs 
mostpopular=df.sort_values('popularity',ascending=False).head(10)


#setting Index
df.set_index("release_date",inplace=True)
df.index=pd.to_datetime(df.index)

#changing duration of milliseconds to seconds

df["duration"]=df["duration_ms"].apply(lambda x: round(x/1000))
df.drop("duration_ms",inplace=True,axis=1)

#corelation map

corr_df=df.drop(["key","mode","explicit"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g",vmin=-1,vmax=-1,center=0,cmap="Blues",linewidths=1,linecolor="Green")
heatmap.set_title("Correlation HeatMap Between Variable")

heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


#creating a sample of data to use for regression line between energy and loudness

sample_df=df.sample(int(0.004*len(df)))

#code for regression line loudness and energy
plt.figure(figsize=(10,6))
sns.regplot(data=sample_df,y="loudness",x="energy",color="c").set(title="Loudness vs Energy")

#code for regression line between popularity and acousticness 

plt.figure(figsize=(10,6))
sns.regplot(data=sample_df,y="popularity",x="acousticness",color="b").set(title="Popularity vs Acousticness")


df['dates']=df.index.get_level_values('release_date')
df.dates=pd.to_datetime(df.dates)
years=df.dates.dt.year


#Songs per year 
sns.displot(years,discrete=True,aspect=2,height=5,kind='hist').set(title="Number os songs per year")


#Bar Graph for duration vs Year
total_dr=df.duration
fig,ax=plt.subplots(figsize=(18,7))
fig=sns.barplot(x=years,y=total_dr,ax=ax,errwidth=False).set(title="Year vs Duration")
plt.xticks(rotation=90)

#Line Graph of Year vs Duration
total_dr=df.duration
sns.set_style(style="whitegrid")
fig_dims=(10,5)
fig, ax=plt.subplots(figsize=fig_dims)
fig=sns.lineplot(x=years,y=total_dr,ax=ax).set(title="year vs Duration")
plt.xticks(rotation=60)

 
#Graph for time comparison of different genres.

df_genre=pd.read_csv('SpotifyFeatures.csv')
plt.title("Duration of the songs in Different Genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y='genre',x='duration_ms',data=df_genre)
plt.xlabel("Duration(ms)")
plt.ylabel("Genres")


#Top 5 Genres by Popularity

sns.set_style(style='darkgrid')
plt.figure(figsize=(10,5))
famous=df_genre.sort_values('popularity',ascending=False).head(10)
sns.barplot(x='popularity',y='genre',data=famous).set(title="Top 5 genres by Popularity")
plt.show()

