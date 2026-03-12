-- ======================================================
-- Script SQL : Base de données du système de supervision
-- ======================================================
-- Ce script permet de créer la base de données utilisée
-- pour stocker les métriques envoyées par les agents
-- du système de monitoring développé en Python.
-- ======================================================


--  Création de la base de données appelée "supervision"
CREATE DATABASE supervision;


-- Sélection de la base de données pour exécuter les commandes suivantes
USE supervision;

CREATE TABLE nodes (

    id INT AUTO_INCREMENT PRIMARY KEY,

    node_name VARCHAR(50),

    os VARCHAR(50),

    cpu INT,

    memory INT,

    disk INT,

    -- Temps de fonctionnement de la machine (uptime) (généralement exprimé en secondes)
    uptime INT,

    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);