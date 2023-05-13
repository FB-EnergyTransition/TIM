# Benutzerhandbuch TIM-Skript

## Einleitung

Dieses Benutzerhandbuch enthält Informationen über das TIM-Skript, mit dem
Daten aus CSV-Dateien in die InfluxDB der Forschung Burgenland hochgeladen werden
können. 

## Installation und Setup

## Beschreibung der Funktionalitäten
Dieses Skript verfügt über 2 Hauptfunktionalitäten:
1. Konvertieren von CSV-Dateien zu Annotated-CSV-Dateien
2. Hochladen der Daten aus den konvertierten Dateien in einen Bucket nach Wahl der InfluxDB der Forschung Burgenland

## Anleitung zum Ausführen des Programms

Zum Ausführen des Programms sind folgende Schritte notwendig:

1. Laden Sie eine Releaseversion des TIM-Projekts von https://github.com/FB-EnergyTransition/TIM herunter.
2. _Optional/Empfohlen:_ Speichern Sie die CSV-Datei, aus der Sie Daten hochladen möchten, im Projektordner "resources" ab.
3. Öffnen Sie ein Terminal (Anaconda/cmd etc.) und navigieren Sie zum Ordner, in dem das Projekt enthalten ist.
4. Stellen Sie die Verbindung zum Proxmox-Server her, in dem die InfluxDB läuft.
5. Führen Sie die main.py Datei aus.

Anaconda:
```
main.py
```
Windows:
```
./main.py
```

6. Das Programm startet und fragt, ob Sie einen Dateiupload vornehmen möchten oder die Voraussetzungen
der CSV-Dateien für einen Dateiupload ausgeben möchten.
Wählen Sie zwischen den Optionen:
- 1 - Upload vornehmen
- 2 - CSV-Voraussetzungen ausgeben
Bei Option 2 werden die Voraussetzungen ausgegeben und Sie erhalten erneut die Möglichkeit zur Auswahl
zwischen diesen beiden Optionen.

7. Wenn Sie Option 1 wählen, werden Sie nach dem Dateipfad gefragt, in dem die hochzuladende CSV-Datei liegt.
Geben Sie diesen Pfad ein.
Falls sich die Datei im "resources"-Ordner befindet, geben Sie Folgendes ein:
```
./resources/[Dateiname].csv
```
Es folgt eine Überprüfung, ob die angegebene Datei existiert und für den Upload 
entsprechend der CSV-Voraussetzungen geeignet ist.

8. Bei Eingabe eines gültigen Pfades folgt die Frage, welche Messungen in dieser Datei
enthalten sind.
Geben Sie den Namen/Überbegriff der Messung ein, z.B. "Strompreis", "Windstärke" etc.
Diese Eingabe wird später als **measurement** in der InfluxDB angezeigt.

9. Anschließend folgt die Frage, in welchen Bucket die Dateien aus der Datei hochgeladen
werden sollen.
Geben Sie den Namen des Buckets ein (auf Groß-/Kleinschreibung achten!).

Es folgt eine Überprüfung, ob der Bucket in der InfluxDB der Forschung Burgenland existiert.

10. Bei gültiger Eingabe werden Sie nun gefragt, ob alle Werte aus der CSV-Datei dieselben Einheiten haben.
Wählen Sie zwischen den folgenden Optionen:
- 1 - Alle Werte haben dieselbe Einheit
- 2 - Die enthaltenen Werte haben unterschiedliche Einheiten

11. Im nächsten Schritt werden Sie je nach Ihrer gewählten Option aufgefordert,
entweder die Einheit für alle Werte einzugeben oder die Einheit für jede Wertespalte
wird einzeln abgefragt.

12. Es folgt der Datenupload. Bei erfolgreichem Upload erhalten Sie eine Bestätigung,
dass die Daten in die InfluxDB hochgeladen wurden.