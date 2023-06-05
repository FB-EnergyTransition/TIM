# TIM - Readme

Das Skript in diesem Repository entstand im Rahmen eines Praxisprojekts einer Studentengruppe der Fachhochschule Burgenland in Zusammenarbeit mit der Forschung Burgenland GmbH.

Ziel des Praxisprojekts war die Einrichtung einer Zeitreihendatenbank (mittels InfluxDB), die Entwicklung eines Python Skripts zum Upload von Daten aus CSV-Dateien in die Datenbank sowie die Einrichtung von Grafana inkl. einer Verknüpfung zu der Datenbank, um die Daten auch visualisieren zu können.

Die InfluxDB sowie Grafana laufen in Docker Containern auf einem Proxmox-Server, der von der Forschung Burgenland für dieses Projekt bereitgestellt wurde. Für den Zugriff darauf ist eine VPN-Verbindung zu diesem Server erforderlich.

Alle Setup- und Installationsanweisungen sowie detaillierte Beschreibungen der Funktionen und Anwendungsmöglichkeiten des Programms befinden sich im [Benutzerhandbuch](user_manual.md).
