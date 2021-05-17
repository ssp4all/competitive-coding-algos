# Write a SQL query to get the second highest salary from the Employee table.

-- https://leetcode.com/problems/second-highest-salary/
SELECT 
	IFNULL
	((SELECT 
			MAX(salary) 
		FROM 
			employee 
		WHERE 
			salary 
		NOT IN 
			(SELECT MAX(salary) 
				FROM employee)), 
	NULL)
AS SecondHighestSalary;

-- upsolving -- gives null if not found solution
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;


######################################################
-- https://leetcode.com/problems/swap-salary
-- Write an SQL query to swap all 'f' and 'm' values 
-- (i.e., change all 'f' values to 'm' and vice versa) with 
-- a single update statement and no intermediate temp table(s).


UPDATE 
	salary 
SET 
	sex = CASE sex 
	        WHEN 'm' THEN 'f'
	        ELSE 'm'
	        END;

######################################################

-- A country is big if it has an
--  area of bigger than 3 million
--   square km or a population of more than 25 million.

-- Write a SQL solution to output 
-- big countries' name, population and area.

# Write your MySQL query statement below
SELECT
    name, population, area
FROM
    world
WHERE
    area > 3000000

UNION

SELECT
    name, population, area
FROM
    world
WHERE
    population > 25000000;

######################################################

-- https://leetcode.com/problems/not-boring-movies
-- Please write a SQL query to output movies with an odd 
-- numbered ID and a
-- description that is not 'boring'. Order the result by rating.

SELECT * 
FROM cinema
WHERE description <> 'boring' AND MOD(id, 2) = 1
ORDER BY rating DESC;

######################################################

