-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Ven 25 Novembre 2022 à 19:19
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `anime_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `animes`
--

CREATE TABLE IF NOT EXISTS `animes` (
  `ANIMEID` int(11) NOT NULL AUTO_INCREMENT,
  `ANIME_NAME` varchar(200) NOT NULL,
  `GENRES` varchar(200) NOT NULL,
  `AUTHOR` varchar(200) NOT NULL,
  `NUMBER_OF_SEASONS` int(11) NOT NULL,
  PRIMARY KEY (`ANIMEID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Contenu de la table `animes`
--

INSERT INTO `animes` (`ANIMEID`, `ANIME_NAME`, `GENRES`, `AUTHOR`, `NUMBER_OF_SEASONS`) VALUES
(1, 'One Piece', 'Adventure, Comedy, Drama, Fantasy', 'Eiichiro Oda', 1),
(2, 'Sword Art Online', 'Action, aventure, fantasy, romance, science-fiction', 'Reki Kawahara', 4),
(3, 'Haikyu!!', 'Comedy , Coming-of-age , Sports', 'Haruichi Furudate', 6);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
