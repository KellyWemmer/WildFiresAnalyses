SELECT FIRE_YEAR, COUNT(*) AS NumberOfFires
FROM Fires
GROUP BY FIRE_YEAR
Order By FIRE_YEAR