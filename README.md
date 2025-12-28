# Rezepte

Dieses Repository ist eine **kuratierte Rezeptsammlung**, gedacht als **lebendes Kochbuch**.
Rezepte liegen als Markdown-Dateien vor, werden mit Git versioniert und über GitBook gerendert.


## Wie das Repository funktioniert

- Jedes Rezept ist eine einzelne `.md`-Datei
- Ordner definieren Kategorien
- Neue Rezepte erscheinen automatisch
- Die Seitenleiste wird automatisch erzeugt


## Wie GitBook daraus ein Kochbuch macht

- Jeder Ordner im Repo wird zu einer **Kategorie (Group)**
- Die Seitenleiste auf Gitbook wird **automatisch via Script** generiert
- Jede Rezeptdatei wird automatisch darunter gelistet

👉 Die Datei `SUMMARY.md` wird **nicht manuell gepflegt** sondern bei jedem Commit **automatisch neu erzeugt**.


## TL;DR

- 📄 Markdown schreiben
- 📁 Ordner anlegen
- ⚙️ Automation erledigt die Navigation
- 📚 GitBook rendert das Ergebnis
