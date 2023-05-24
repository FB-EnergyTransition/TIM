# Benutzerhandbuch TIM

<img src="./pics/Logo.png" width = 300>

## Inhaltsverzeichnis
1. Einleitung
2. Setup- und Installationsanweisungen
3. Beschreibung der Funktionalitäten des Programms
4. Voraussetzungen für hochzuladende CSV-Dateien
5. Anleitung zum Ausführen des Programms

## Einleitung
Dieses Benutzerhandbuch enthält Informationen über das TIM-Skript, einer Kommandozeilen-Applikation, mit der
Daten aus CSV-Dateien in die InfluxDB der Forschung Burgenland hochgeladen werden können. 

## Setup- und Installationsanweisungen
Grundsätzlich kann das Programm entweder über das Betriebssystem-eigene Terminal oder über eine Anaconda-Installation
aufgerufen werden. Letztere ist auf allen Betriebssystemen anwendbar.
Die Anweisungen in diesem Benutzerhandbuch werden sowohl für eine Anaconda-Installation als auch für eine Ausführung
auf einem Windows-Betriebssystem über die Eingabeaufforderung (cmd) beschrieben.

### Python-Setup
Zunächst ist für das Setup eine Python-Installation erforderlich.
Hier finden Sie die Schritte, um Python entweder lokal auf Ihrem Windows-PC oder mittels Anaconda zu installieren.

#### Python Installation auf Windows
- Laden Sie auf der [Python-Webseite](https://www.python.org/downloads/) eine Python-Version für Windows herunter.
Für dieses Programm ist mindestens die Version 3.9 erforderlich.
- Führen Sie die heruntergeladene .exe-Datei aus.
- Aktivieren Sie die Option "**Add Python [Versionsnummer] to PATH**", optional auch die andere Option "**Install launcher
for all users**".
- Klicken Sie auf "**Install Now**".
- Nach Beenden der Installation öffnen Sie die Eingabeaufforderung (cmd) und tippen Sie `python` ein.
Sie sollten die Python-Versionsnummer sehen und die Möglichkeit haben, Python-Befehle direkt auszuführen.
Wenn dies der Fall ist, war die Installation erfolgreich und Sie können diesen Modus mit der Eingabe `quit()` beenden.
- Falls die Installation nicht erfolgreich war, überprüfen Sie die erhaltene Fehlermeldung.

#### Anaconda
- Gehen Sie auf die [Anaconda-Webseite](https://docs.anaconda.com/free/anaconda/install/).
- Wählen Sie die Installation für Ihr jeweiligen Betriebssystem, z.B. Windows, Linux oder macOS aus.
- Folgen Sie den Anweisungen des jeweiligen Installationstutorials.
- Öffnen Sie die mitinstallierte Anaconda Prompt und geben Sie python ein.
Sie sollten die Python-Versionsnummer sehen und die Möglichkeit haben, Python-Befehle direkt auszuführen.
Wenn dies der Fall ist, war die Installation erfolgreich und Sie können diesen Modus mit der Eingabe `quit()` beenden.
- Falls die Installation nicht erfolgreich war, überprüfen Sie die erhaltene Fehlermeldung.

### Einrichten der Verbindung zum Proxmox-Server
Sowohl die InfluxDB als auch die Grafana-Installation befinden sich auf einem virtuellen Proxmox-Server
der Forschung Burgenland. Um mit den Daten aus der InfluxDB arbeiten zu können bzw. Daten hochladen zu können,
muss vorab eine Verbindung zu diesem Server hergestellt werden.

#### VPN-Verbindung einrichten
- Installieren Sie einen VPN-Client, wie z.B. [OpenVPN](https://openvpn.net/community-downloads/).
- Erstellen Sie ein neues VPN-Profil. Die dazu benötigten Dateien befinden sich in [diesem zip-Ordner](https://fhburgenlandat-my.sharepoint.com/:u:/g/personal/2110859020_fh-burgenland_at/EUZN9nb_jmxGr0PP_ChDXGcB4fUma-cF6e4kvUgD05qB6g?e=DQqgIq).
- Stellen Sie die Verbindung über das neu erstellte Profil her.

#### Verbindung über Client wie PuTTy herstellen
- Installieren Sie einen SSH-Client, wie z.B. [PuTTY](https://www.putty.org/).
- Geben Sie die IP-Adresse aus den [Zugangsdaten](https://fhburgenlandat-my.sharepoint.com/:w:/g/personal/2110859020_fh-burgenland_at/ES3bm27Xxo5Kvng_sYOS7FABGoU2h7Xpae6BbvKCAkGtEg?e=dnsajV)
ein und klicken Sie auf Verbinden.
- Es öffnet sich ein Terminalfenster. Geben Sie den Benutzernamen und das Passwort aus den [Zugangsdaten](https://fhburgenlandat-my.sharepoint.com/:w:/g/personal/2110859020_fh-burgenland_at/ES3bm27Xxo5Kvng_sYOS7FABGoU2h7Xpae6BbvKCAkGtEg?e=dnsajV) ein.
- Die Verbindung zum Server wird hergestellt. Falls nicht, überprüfen Sie die erhaltene Fehlermeldung.

#### Desktop-Zugriff über Remote Desktop
Falls Sie auch einen Zugriff auf das Desktop des Servers wünschen, z.B. für die Visualisierung der Daten in Grafana,
sind folgende Schritte zu befolgen:
- Wenn noch nicht vorhanden, installieren Sie einen Desktop-Client Ihrer Wahl. Auf Windows können Sie mit der vorinstallierten
Remotedesktop-App arbeiten.
- Erstellen Sie, je nach Client, ein neues Desktop/eine neue Desktopverbindung.
- Verwenden Sie zur Einrichtung der Verbindung zum Proxmox-Server der Forschung Burgenland dieselben [Zugangsdaten](https://fhburgenlandat-my.sharepoint.com/:w:/g/personal/2110859020_fh-burgenland_at/ES3bm27Xxo5Kvng_sYOS7FABGoU2h7Xpae6BbvKCAkGtEg?e=dnsajV) wie zuvor.
- Das Passwort zum Zugriff auf das Desktop ist dasselbe wie in den Zugangsdaten.
- Bei erfolgreichem Zugriff sollten Sie das Desktop einer Ubuntu-Maschine sehen.

### Installation Python Packages
Die nachfolgenden Python Packages müssen installiert werden, um das Programm ausführen zu können.
Die Installation erfolgt mit `pip install [Packagename]`.
- influxdb
- influxdb_client

## Beschreibung der Funktionalitäten
Dieses Skript verfügt über 2 Hauptfunktionalitäten:

### Konvertieren von CSV-Dateien zu Annotated-CSV-Dateien
Um die gewünschten Daten aus den CSV-Dateien hochladen zu können, müssen diese zunächst aufbereitet und in sogenannte annotated csvs konvertiert werden.
So wird sichergestellt, dass beim Upload in die InfluxDB alle entsprechenden Daten, Parameter und Metadaten korrekt gesetzt sind bzw. ausgelesen werden.

### Hochladen der Daten aus den konvertierten Dateien in einen Bucket nach Wahl der InfluxDB der Forschung Burgenland
Mithilfe der Eingabe bestimmter Parameter können die ausgelesenen Daten im Anschluss in einen Bucket nach Wahl in die InfluxDB
der Forschung Burgenland hochgeladen werden. Für die Eingabe der noch fehlenden Parameter stellt das Programm eine
Benutzeroberfläche bereit, in der der User nach den Parametern gefragt wird.

## Voraussetzungen für hochzuladende CSV-Dateien
Es gibt einige Voraussetzungen für CSV-Dateien, damit Daten daraus in die InfluxDB hochgeladen werden können.
Die folgenden Anforderungen gelten für alle CSV-Dateien, die als Eingabeparameter für dieses Program verwendet werden:

1. Das Trennzeichen in den CSV-Dateien muss das Komma (",") sein, nicht das Semikolon (";").
2. Als Dezimaltrennzeichen muss der Punkt ("."), nicht das Komma (",") verwendet werden.
Ansonsten können die numerischen Werte nicht ermittelt werden.
3. Zeitstempel müssen und können sich ausschließlich in der ersten Spalte befinden.
4. Zeitstempel müssen im Format "dd.MM.YYYY HH:mm:ss" vorhanden sein.
5. Numerische Werte starten ab der zweiten Spalte. Diese Spalten dürfen nur gültige numerische Werte (Integers oder
Floats) enthalten.
6. Die Spaltenbezeichnungen sollten die spezifischen Bezeichnungen der in der jeweiligen Spalte enthaltenen Messwerte
enthalten. Diese dienen in der InfluxDB als "field"-Bezeichnungen.

## Anleitung zum Ausführen des Programms
Zum Ausführen des Programms sind zusätzlich zu den oben beschriebenen Anweisungen die folgenden Setups/Schritte notwendig:
1. Benötigte Umgebung:
   - mind. Python 3.9
2. Laden Sie eine Releaseversion des TIM-Projekts von https://github.com/FB-EnergyTransition/TIM herunter.
3. _Optional/Empfohlen:_ Speichern Sie die CSV-Datei, aus der Sie Daten hochladen möchten, im Projektordner "resources" ab.
4. Öffnen Sie ein Terminal (Anaconda/cmd etc.) und navigieren Sie zum Ordner, in dem das Projekt enthalten ist.
5. Stellen Sie die Verbindung zum Proxmox-Server her, in dem die InfluxDB läuft.
6. Führen Sie die main.py Datei aus.

Anaconda:
```
python main.py
```
Windows:
```
./main.py
```

7. Das Programm startet und fragt, ob Sie einen Dateiupload vornehmen möchten oder die Voraussetzungen
der CSV-Dateien für einen Dateiupload ausgeben möchten.
Wählen Sie zwischen den Optionen:
- 1 - Upload vornehmen
- 2 - CSV-Voraussetzungen ausgeben
Bei Option 2 werden die Voraussetzungen ausgegeben und Sie erhalten erneut die Möglichkeit zur Auswahl
zwischen diesen beiden Optionen.

8. Wenn Sie Option 1 wählen, werden Sie nach dem Dateipfad gefragt, in dem die hochzuladende CSV-Datei liegt.
Geben Sie diesen Pfad ein.
Falls sich die Datei im "resources"-Ordner befindet, geben Sie Folgendes ein:
```
./resources/[Dateiname].csv
```
Es folgt eine Überprüfung, ob die angegebene Datei existiert und für den Upload 
entsprechend der CSV-Voraussetzungen geeignet ist.

9. Bei Eingabe eines gültigen Pfades folgt die Frage, welche Messungen in dieser Datei
enthalten sind.
Geben Sie den Namen/Überbegriff der Messung ein, z.B. "Strompreis", "Windstärke" etc.
Diese Eingabe wird später als **measurement** in der InfluxDB angezeigt.

10. Anschließend folgt die Frage, in welchen Bucket die Dateien aus der Datei hochgeladen
werden sollen.
Geben Sie den Namen des Buckets ein (auf Groß-/Kleinschreibung achten!).

Es folgt eine Überprüfung, ob der Bucket in der InfluxDB der Forschung Burgenland existiert.

11. Bei gültiger Eingabe werden Sie nun gefragt, ob alle Werte aus der CSV-Datei dieselben Einheiten haben.
Wählen Sie zwischen den folgenden Optionen:
- 1 - Alle Werte haben dieselbe Einheit
- 2 - Die enthaltenen Werte haben unterschiedliche Einheiten

12. Im nächsten Schritt werden Sie je nach Ihrer gewählten Option aufgefordert,
entweder die Einheit für alle Werte einzugeben oder die Einheit für jede Wertespalte
wird einzeln abgefragt.

13. Es folgt der Datenupload. Bei erfolgreichem Upload erhalten Sie eine Bestätigung,
dass die Daten in die InfluxDB hochgeladen wurden.