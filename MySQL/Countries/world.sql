SELECT name, language, percentage 
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id;

SELECT countries.name, count(*) AS cities
FROM cities
LEFT JOIN countries
ON cities.country_id = countries.id
GROUP by cities.country_id
ORDER by cities DESC;

SELECT cities.name, cities.population
FROM cities
LEFT JOIN countries
ON cities.country_code = countries.code
WHERE countries.name = 'Mexico' and cities.population > 500000
ORDER by population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE percentage > 89
ORDER by percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 and population > 100000;

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;

SELECT countries.name, cities.district, cities.name, cities.population
FROM cities
LEFT JOIN countries
ON cities.country_id = countries.id
WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;

SELECT countries.region AS region, count(countries.region) AS countries
FROM countries
GROUP by region
ORDER by countries DESC