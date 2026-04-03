SELECT Department, Employee, Salary
FROM (SELECT D.name AS Department, E.name As Employee, E.Salary, DENSE_RANK() OVER (PARTITION BY D.id ORDER BY E.salary DESC) AS RANKING
        FROM Employee E JOIN Department D ON E.departmentId = D.id
        GROUP BY D.id, E.name
        ORDER BY D.id, E.salary DESC) A
WHERE RANKING <= 3;
