# Checking duplicated values
SELECT Title
FROM moviedata
GROUP BY Title
HAVING COUNT(Title) > 2;

#1 Display number of movies for each year
SELECT Year, COUNT(Title) AS "Movies per Year"
FROM moviedata
GROUP BY Year
ORDER BY Year;

#2 Classify movies based on rating
SELECT Title, Actors,
CASE 
    WHEN Rating >= 7 THEN "Excellent"
    WHEN Rating >= 6 THEN "Good"
    ELSE "Average"
END AS Rating_Category
FROM moviedata
ORDER BY Rating DESC;

#3 Display the title of the top 10 movies with the highest revenue
SELECT Title
FROM moviedata
ORDER BY Revenue_millions DESC
LIMIT 10;

#4 Display title and director of the top 10 movies with the highest rating
SELECT Title, Director
FROM moviedata
ORDER BY Rating DESC
LIMIT 10;

#5 Display the average rating for each year
SELECT Year, AVG(Rating) AS "Average Rating"
FROM moviedata
GROUP BY Year
ORDER BY Year;

#6 Display the title of movies having a runtime >= 180 minutes
SELECT Title
FROM moviedata
WHERE Runtime_minutes >= 180;

#7 Count number of action movies
SELECT COUNT(Genre)
FROM moviedata
WHERE upper(Genre) LIKE "%ACTION%";

#8 Display the director that has produced more movies 
SELECT Director, COUNT(Title) AS "Movies per Director"
FROM moviedata
GROUP BY Director
ORDER BY COUNT(Title) DESC
LIMIT 10;

#9 Do movies directed by Christopher Nolan have good ratings? 
SELECT Title, Rating,
CASE 
    WHEN Rating >= 7 THEN "Excellent"
    WHEN Rating >= 6 THEN "Good"
    ELSE "Average"
END AS Rating_Category
FROM moviedata
WHERE upper(Director) LIKE "%CHRISTOPHER NOLAN%"
ORDER BY Rating DESC;

#10 Do movies starred by Christian Bale have good ratings? 
SELECT Title, Rating,
CASE 
    WHEN Rating >= 7 THEN "Excellent"
    WHEN Rating >= 6 THEN "Good"
    ELSE "Average"
END AS Rating_Category
FROM moviedata
WHERE upper(Actors) LIKE "%CHRISTIAN BALE%"
ORDER BY Rating DESC;

#11 Display the title of excellent action movies 
SELECT Title, Genre,
CASE 
    WHEN Rating >= 7 THEN "Excellent"
    WHEN Rating >= 6 THEN "Good"
    ELSE "Average"
END AS Rating_Category
FROM moviedata
WHERE upper(Genre) LIKE "%ACTION%" 
AND Rating >= 7
ORDER BY Rating DESC;

#12 Display the total revenue for each director, sorted by the highest revenue
SELECT Director, SUM(Revenue_millions) AS TotalRevenue
FROM moviedata
GROUP BY Director
ORDER BY TotalRevenue DESC;

#13 Display the top 5 movies with the highest rating-to-revenue ratio (low revenue despite a good rating)
SELECT Title, Rating, Revenue_millions, Rating/Revenue_millions AS RatingToRevenueRatio
FROM moviedata
WHERE Revenue_millions > 0
ORDER BY RatingToRevenueRatio DESC
LIMIT 5;

#14 Display the top 10 average rating for each director, considering only movies released in the last 10 years
SELECT Director, AVG(Rating) AS AvgRating
FROM moviedata
WHERE Year >= YEAR(CURDATE()) - 10
GROUP BY Director
ORDER BY AvgRating DESC
LIMIT 10;

#15 Display the highest-grossing movie for each year
SELECT m1.Year, m1.Title, m1.Director, m1.Revenue_millions
FROM moviedata AS m1
JOIN (
    SELECT Year, MAX(Revenue_millions) AS MaxRevenue
    FROM moviedata
    GROUP BY Year
) m2 
ON m1.Year = m2.Year 
AND m1.Revenue_millions = m2.MaxRevenue
ORDER BY Year;

#16 Display top 5 most common directors in the top 10 movies with the highest rating
WITH Top10Movies AS (
    SELECT Title, Director
    FROM moviedata
    ORDER BY Rating DESC
    LIMIT 10
)
SELECT Director, COUNT(*) AS MovieCount
FROM Top10Movies
GROUP BY Director
ORDER BY MovieCount DESC;

#17 Display top 5 most common directors in the top 10 movies with the highest revenue
WITH Top10Movies AS (
    SELECT Title, Director
    FROM moviedata
    ORDER BY Revenue_millions DESC
    LIMIT 10
)
SELECT Director, COUNT(*) AS MovieCount
FROM Top10Movies
GROUP BY Director
ORDER BY MovieCount DESC;

#18 Display movies with the same director
SELECT Title, Director, COUNT(*)OVER (PARTITION BY Director ORDER BY Director) AS "Count of Movies"
FROM moviedata;







