import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Loading data
data = pd.read_csv("C:/Users/alice/Desktop/Projects/IMDB_project/IMDB-Movie-Data.csv")

# Checking data
print(data.head(5))
print(data.tail(5))

ds = data.shape
print("Number of Rows:", ds[0])
print("Number of Columns:", ds[1])

data.info()

# Checking null values
null_data = data.isnull().values.any()
print("Are there any missing values?", null_data)
data.dropna(inplace=True)

# Checking duplicated values
dup_data = data.duplicated().values.any()
print("Are there any duplicated values?", dup_data)
# If there are duplicated values:
# data.drop_duplicates(inplace=True)

# Data cleaning
data['Genre'] = data['Genre'].str.lower().str.strip()
data['Title'] = data['Title'].str.lower()
data['Director'] = data['Director'].str.title()
data['Actors'] = data['Actors'].str.title()

# Checking after data cleaning
print(data.describe())
data.info()

# 1.Display the title of movies having a runtime >= 180 minutes
print(data[data['Runtime (Minutes)'] >= 180]['Title'])

# 2.Display the average voting for each year
print(data.groupby('Year')['Votes'].mean().sort_values(ascending=False))
sns.barplot(x='Year', y='Votes', data=data, color='mediumaquamarine')
plt.title('Votes per Year')
plt.show()

# 3.Display the average revenue for each year
print(data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False))
sns.barplot(x='Year', y='Revenue (Millions)', data=data, color='mediumaquamarine')
plt.title('Revenue per Year')
plt.show()

# 4.Display the average rating for each director
print(data.groupby('Director')['Rating'].mean().sort_values(ascending=False))

# 5.Display the average rating for each year
avg_rating = data.groupby('Year')['Rating'].mean().sort_values(ascending=False)

# 6.Display title and runtime of the top 10 longest movies
top10_len = data.nlargest(10, 'Runtime (Minutes)')[['Title', 'Runtime (Minutes)']].set_index('Title')
print(top10_len)
sns.barplot(x='Runtime (Minutes)', y=top10_len.index, data=top10_len, color='mediumaquamarine')
plt.title('Top 10 longest Movies')
plt.show()

# 7.Display number of movies for each year
print(data['Year'].value_counts())
sns.countplot(x='Year', data=data, color='mediumaquamarine')
plt.title('Number of Movies per Year')
plt.show()

# 8.Display the title of the movie with the highest revenue
max_revenue = data['Revenue (Millions)'].max()
print(data[max_revenue == data['Revenue (Millions)']]['Title'])

# 9.Display title and director of the top 10 movies with the highest rating
top10_rating = data.nlargest(10, 'Rating')[['Title', 'Rating', 'Director', 'Actors']].set_index('Title')
sns.barplot(x='Rating', y=top10_rating.index, data=top10_rating, hue='Director', dodge=False, color='mediumaquamarine')
plt.legend(bbox_to_anchor=(1, 1), loc=1)
plt.title('Top 10 Highest Rated Movies')
plt.show()

# 10.Display the title of the top 10 movies with the highest revenue
top10_revenue = data.nlargest(10, 'Revenue (Millions)')[['Title', 'Revenue (Millions)', 'Director', 'Actors']]\
                .set_index('Title')
sns.barplot(x='Revenue (Millions)', y=top10_revenue.index, data=top10_revenue, color='mediumaquamarine')
plt.title('Top 10 Highest Revenue Movies')
plt.show()

# 11.Does rating affect the revenue?
sns.scatterplot(x='Rating', y='Revenue (Millions)', data=data, color='mediumaquamarine')
plt.title('Does Rating affect the Revenue?')
plt.show()

# 12.Classify movies based on rating


def rating(rates):
    if rates >= 7.0:
        return 'Excellent'
    elif rates >= 6.0:
        return 'Good'
    else:
        return 'Average'


data['rating_cat'] = data['Rating'].apply(rating)
print(data.head())

# 13.Count number of action movies
print(data['Genre'].dtype)
print(len(data[data['Genre'].str.contains('Action', case=False)]))

# 14.Display unique values from genre (first method)
print(data['Genre'])
list1 = []
for value in data['Genre']:
    list1.append(value.split(','))
print(list1)

one_d = []
for item in list1:
    for item1 in item:
        one_d.append(item1)
print(one_d)

uni_list = []
for item in one_d:
    if item not in uni_list:
        uni_list.append(item)

print(uni_list)

# 15.Display how many movies of each genre were made (first method)
print(Counter(data.Genre.apply(lambda x: pd.Series(x.split(','))).stack().values))

# Display all genres
all_genres = data['Genre'].str.split(',').explode().str.strip()

# 16.Display unique values from genre (second method)
unique_genres = all_genres.unique()
print(unique_genres)

# 17.Display how many movies of each genre were made (second method)
genre_counts = all_genres.value_counts()
print(genre_counts)

# 18.Visualize the distribution of movie genres
sns.barplot(x=genre_counts.index, y=genre_counts.values, color='mediumaquamarine')
plt.xticks(rotation=90)
plt.xlabel('Genres')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Genres')
plt.show()

# 19.Analyze distribution of directors
director_counts = data['Director'].value_counts().nlargest(10)
print(director_counts)

# 20.Visualize the top 10 directors with the most movies
sns.barplot(x=director_counts.index, y=director_counts.values, color='mediumaquamarine')
plt.xticks(rotation=90)
plt.xlabel('Directors')
plt.ylabel('Number of Movies')
plt.title('Top 10 Directors with Most Movies')
plt.show()

# 21.Analyze distribution of actors
all_actors = data['Actors'].str.split(',').explode().str.strip()
actor_counts = all_actors.value_counts().nlargest(10)
print(all_actors)
print(actor_counts)

# 22.Visualize the top 10 actors with the most movies
sns.barplot(x=actor_counts.index, y=actor_counts.values, color='mediumaquamarine')
plt.xticks(rotation=90)
plt.xlabel('Actors')
plt.ylabel('Number of Movies')
plt.title('Top 10 Actors with Most Movies')
plt.show()

# 23.Visualize top 3 movies with high revenue and ratings below the 15th percentile
plt.scatter(data['Revenue (Millions)'], data['Rating'], s=80, alpha=0.7, color='mediumaquamarine')
plt.xlabel('Revenue (Millions)')
plt.ylabel('Rating')
plt.title('Revenue vs. Rating')
# Calculate the 15th percentile of ratings
rating_15th_percentile = data['Rating'].quantile(0.15)
print("The 15th percentile is: " + str(rating_15th_percentile))
# Identify movies with high revenue and low rating (below the 15th percentile)
high_revenue_low_rating = data[data['Rating'] < rating_15th_percentile].nlargest(3, 'Revenue (Millions)')
# Annotate the outliers on the plot
for index, row in high_revenue_low_rating.iterrows():
    plt.annotate(row['Title'], (row['Revenue (Millions)'], row['Rating']),
                 textcoords="offset points", xytext=(0, 10), ha='center')
plt.grid()
plt.show()

print("Top Movies with High Revenue and Low Rating:")
for index, row in high_revenue_low_rating.iterrows():
    print("Title: " + row['Title'])
    print("Revenue (Millions): " + str(row['Revenue (Millions)']))
    print("Rating: " + str(row['Rating']))
    print("-" * 30)

# 24.Display top 5 most common actors in the top 10 movies with the highest rating
top10_actors_df_rating = top10_rating['Actors'].str.split(', ').explode().reset_index(drop=True)
top5_common_actors_rating = top10_actors_df_rating.value_counts().nlargest(5)
print(top5_common_actors_rating)

# 25.Display top 5 most common actors in the top 10 movies with the highest revenue
top10_actors_df_revenue = top10_revenue['Actors'].str.split(', ').explode().reset_index(drop=True)
top5_common_actors_revenue = top10_actors_df_revenue.value_counts().nlargest(5)
print(top5_common_actors_revenue)

# 26.Display top 5 most common directors in the top 10 movies with the highest rating
top10_dir_df_rating = top10_rating['Director'].reset_index(drop=True)
top5_common_dir_rating = top10_dir_df_rating.value_counts().nlargest(5)
print(top5_common_dir_rating)

# 27.Display top 5 most common directors in the top 10 movies with the highest revenue
top10_dir_df_revenue = top10_revenue['Director'].reset_index(drop=True)
top5_common_dir_revenue = top10_dir_df_revenue.value_counts().nlargest(5)
print(top5_common_dir_revenue)
