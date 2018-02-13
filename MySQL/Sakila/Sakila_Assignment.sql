	SELECT first_name, last_name, email, address
    FROM customer
    JOIN address
    ON address.address_id = customer.address_id
    WHERE address.city_id = 312;
    
    SELECT title, description, release_year, rating, special_features, category.name AS genre
    FROM film
    JOIN film_category
    ON film_category.film_id = film.film_id
    JOIN category
    ON category.category_id = film_category.category_id
    WHERE category.name = 'comedy';
    
   SELECT actor.actor_id, actor.first_name, film.title, film.description, film.release_year
   FROM film
   JOIN film_actor
   ON film_actor.film_id = film.film_id
   JOIN actor
   ON actor.actor_id = film_actor.actor_id
   WHERE actor.actor_id = 5;
   
   SELECT first_name, last_name, email, address
   FROM customer
   JOIN store 
   ON store.store_id = customer.store_id
   JOIN address
   ON address.address_id = store.address_id
   WHERE customer.store_id = 1 or city_id = 1 or 42 or 312 or 459;
   
   SELECT title, description, release_year, rating, special_features
   FROM film
   WHERE rating = 'G' and special_features like '%behind_the_scenes%';
   
   SELECT film.film_id, film.title, film_actor.actor_id,  concat_ws(' ', actor.first_name, actor.last_name) as 'actor_name'
   FROM film
   JOIN film_actor
   ON film_actor.film_id = film.film_id
   JOIN actor
   ON actor.actor_id = film_actor.actor_id
   WHERE film.film_id = 369;
   
   SELECT title, description, release_year, rating, special_features, category.name as genre, rental_rate
   FROM film
   JOIN film_category
   ON film_category.film_id = film.film_id
   JOIN category
   ON category.category_id = film_category.category_id
   WHERE category.name = 'drama' and rental_rate = 2.99;
   
   SELECT title, description, release_year, rating, special_features, category.name as genre, concat_ws(' ', actor.first_name, actor.last_name) as 'actor_name'
   FROM film
   JOIN film_category
   ON film_category.film_id = film.film_id
   JOIN category
   ON category.category_id = film_category.category_id
   JOIN film_actor
   ON film_actor.film_id = film.film_id
   JOIN actor
   ON actor.actor_id = film_actor.actor_id
   WHERE category.name = 'action' and actor.first_name = 'Sandra' and actor.last_name = 'Kilmer';
   