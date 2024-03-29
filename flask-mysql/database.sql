CREATE DATABASE IF NOT EXISTS `sampleprofile` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8_general_ci;
use `sampleprofile`;

create table if not exists `accounts` (
	`id` int(11) NOT NULL auto_increment,
    `username` varchar(50) not null,
    `password` varchar(255) not null,
    `email` varchar(100) not null,
    `organisation` varchar(100) not null,
    `address` varchar(100) not null,
    `city` varchar(100) not null,
    `state` varchar(100) not null,
    `country` varchar(100) not null,
    `postalcode` varchar(100) not null,
    primary key (`id`)
) engine=InnoDB auto_increment=1 default charset=utf8mb4;
