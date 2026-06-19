SELECT*FROM providers;
SELECT*FROM food;
SELECT*FROM claims;
SELECT*FROM receivers;

SELECT City,
COUNT(*) AS Providers
FROM providers
GROUP BY City;

SELECT City,
COUNT(*) AS Providers
FROM providers
GROUP BY City;

SELECT Provider_Type,
SUM(Quantity) AS TotalFood
FROM food
GROUP BY Provider_Type
ORDER BY TotalFood DESC;

SELECT Name,
       Contact,
       City
FROM providers
WHERE Name = 'Blackwell Ltd'
  AND City = 'South Jeffrey';

SELECT Receiver_ID,
COUNT(*) AS Claims
FROM claims
GROUP BY Receiver_ID
ORDER BY Claims DESC;

SELECT SUM(Quantity)
FROM food;

SELECT Location,
COUNT(*) AS Listings
FROM food
GROUP BY Location
ORDER BY Listings DESC;

SELECT Food_Type,
COUNT(*)
FROM food
GROUP BY Food_Type;

SELECT Food_ID,
COUNT(*) AS Claims
FROM claims
GROUP BY Food_ID;

SELECT p.Name,
COUNT(*) AS SuccessClaims
FROM claims c
JOIN food f
ON c.Food_ID=f.Food_ID
JOIN providers p
ON f.Provider_ID=p.Provider_ID
WHERE c.Status='Completed'
GROUP BY p.Name
ORDER BY SuccessClaims DESC;

SELECT Status,
COUNT(*)*100.0/
(SELECT COUNT(*) FROM claims)
AS Percentage
FROM claims
GROUP BY Status;

SELECT c.Receiver_ID,
AVG(f.Quantity)
FROM claims c
JOIN food f
ON c.Food_ID=f.Food_ID
GROUP BY c.Receiver_ID;

SELECT Meal_Type,
COUNT(*) AS Total
FROM claims c
JOIN food f
ON c.Food_ID=f.Food_ID
GROUP BY Meal_Type
ORDER BY Total DESC;


SELECT Provider_ID,
SUM(Quantity)
FROM food
GROUP BY Provider_ID;

SELECT *
FROM food
WHERE Expiry_Date<GETDATE();

SELECT f.Location,
       COUNT(*) AS Successful_Claims
FROM claims c
JOIN food f
ON c.Food_ID = f.Food_ID
WHERE c.Status = 'Completed'
GROUP BY f.Location
ORDER BY Successful_Claims DESC;

SELECT TOP 10
       f.Food_Name,
       COUNT(c.Claim_ID) AS Total_Claims
FROM food f
JOIN claims c
ON f.Food_ID = c.Food_ID
GROUP BY f.Food_Name
ORDER BY Total_Claims DESC;

SELECT Provider_Type,
       AVG(Quantity) AS Avg_Quantity_Donated
FROM food
GROUP BY Provider_Type
ORDER BY Avg_Quantity_Donated DESC;