SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM users
LEFT JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as users2
ON users.id = friendships.friend_id;

SELECT * FROM Friendship.users;
INSERT INTO `Friendship`.`users` (`id`, `first_name`, `last_name`, `created_at`) VALUES ('1', 'Chris', 'Fowler', '2018-01-26 22:00:00');
INSERT INTO `Friendship`.`users` (`id`, `first_name`, `last_name`, `created_at`) VALUES ('2', 'James', 'Johnson', '2018-01-26 22:00:00');
INSERT INTO `Friendship`.`users` (`id`, `first_name`, `last_name`, `created_at`) VALUES ('3', 'Diana', 'Smith', '2018-01-26 22:00:00');
INSERT INTO `Friendship`.`users` (`id`, `first_name`, `last_name`, `created_at`) VALUES ('4', 'Jessica', 'Davidson', '2018-01-26 22:00:00');

SELECT * FROM Friendship.friendships
INSERT INTO `Friendship`.`friendships` (`id`, `created_at`, `updated_at`, `user_id`, `friend_id`) VALUES ('1', '2018-01-26 22:00:00', '2018-01-26 22:00:00', '1', '4');
INSERT INTO `Friendship`.`friendships` (`id`, `created_at`, `updated_at`, `user_id`, `friend_id`) VALUES ('2', '2018-01-26 22:00:00', '2018-01-26 22:00:00', '2', '3');
INSERT INTO `Friendship`.`friendships` (`id`, `created_at`, `updated_at`, `user_id`, `friend_id`) VALUES ('3', '2018-01-26 22:00:00', '2018-01-26 22:00:00', '3', '2');
INSERT INTO `Friendship`.`friendships` (`id`, `created_at`, `updated_at`, `user_id`, `friend_id`) VALUES ('4', '2018-01-26 22:00:00', '2018-01-26 22:00:00', '4', '1');
