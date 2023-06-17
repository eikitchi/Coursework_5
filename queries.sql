--создание базы данных
CREATE DATABASE head_hunter;

--создание таблиц
CREATE TABLE IF NOT EXISTS employers
(
	employer_id int PRIMARY KEY,
	employer_name varchar(255) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS vacancies
(
	vacancy_id int PRIMARY KEY,
	vacancy_name varchar(255) NOT NULL,
	employer_id int REFERENCES employers(employer_id) NOT NULL,
	city text,
	url text,
	salary int
);
INSERT INTO employers(employer_id, employer_name, employer_url)
VALUES(%s, %s, %s)
ON CONFLICT (employer_id) DO NOTHING, (employer_id, employer, employer_url)


INSERT INTO vacancies(vacancy_id, vacancy_name, employer_id,
description, url, payment_from, payment_to, date_published)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (vacancy_id) DO NOTHING, (vacancy_id, vacancy_name, employer_id, description, url,
payment_from, payment_to, date_published)

--companies_and_vacancies_count
SELECT employer_name, COUNT(*) as quantity_vacancies
FROM vacancies
LEFT JOIN employers USING(employer_id)
GROUP BY employer_name
ORDER BY quantity_vacancies DESC, employer_name

--all_vacancies
SELECT employers.employer_name, vacancy_name, salary_max, url
FROM vacancies
JOIN employers USING(employer_id)
WHERE salary_max IS NOT NULL
ORDER BY salary_max DESC, vacancy_name

--avg_salary
SELECT ROUND(AVG(salary_max)) as average_salary
FROM vacancies

--vacancies_with_higher_salary
SELECT vacancy_name, salary_max
FROM vacancies
WHERE salary_max > (SELECT AVG(salary_max) FROM vacancies)
ORDER BY salary_max DESC, vacancy_name

--
SELECT vacancy_name
FROM vacancies
WHERE vacancy_name ILIKE '%python%'
ORDER BY vacancy_name
