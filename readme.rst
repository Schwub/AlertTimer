===============================================================================
Schrollis LARP-Countdown
===============================================================================

:Author: Michael Schwab
:Date: 2017-02-24

.. inhalt::
.. sectnum::

Aufruf
======

Das Programm kann über folgende Wege aufgerufen werden:

1. Unter Windows kann das Programm **TimerSetup.exe**, das sich in dem Ordner
   */dist/TimerSetup* befindet, ausgeführt werden.
2. Das Pythonscript **SetupTimer** kann mit dem **Python3-Interpreter**
   aufgerufen werden, das Modul **PyQt4** muss auf dem Rechner installiert sein.

Setup-Fenster
=============

- In dem Feld *Password* muss das Passwort für den Timer eingetragen werden,
  es darf höchstens 17 Zeichen lang sein und darf nur aus Ziffern bestehen.

- In dem Feld *Totaltime* wird die Startzeit des Countdowns eingetragen. Die
  Zeit muss größer als 00:00:00 sein.

- In dem Feld *Timepunishment* wird die Zeit eingetragen, die den Spielern
  bei der Eingabe eines falschen Passwords abgezogen wird. Sollte 
  für *Timepunishment* eine längere Zeit als für *Totaltime* eingetragen sein,
  wird beim Start eine Meldung ausgegeben.
  Mit *Yes* wird der Timer normal gestartet, 
  mit *No* wird der Start abgebrochen.

- Der *Start*-Knopf startet den Timer.



Standby
=======

Zunächst befindet sich der Timer im *Standby-Modus*. In diesem Modus wird 
lediglich die gesetzte Zeit auf dem Bildschirm angezeigt, durch einen Mausklick
oder das betätigen der *Leer*-Taste wird der Countdown gestartet.

Countdown
=========

Im Countdown Modus läuft ein Timer von der gesetzten Zeit gegen Null. 
Platzhalter-Symbole geben einen Hinweis auf die Länge des gestzten 
Passworts. Die Spieler können nun ein Passwort eingeben und überprüfen lassen.
Sollten die Spieler ein falsches Passwort überprüfen, wird eine blinckende
Meldung angezeigt und eine Zeitstrafe(falls diese gesetzt wurde) wird von der 
restlichen Zeit abgezogen.
Sollten die Spieler das richtige Passwort eingeben wird der Timer gestoppt
und eine Erfolgsmeldung erscheint auf dem Bildschirm. Sollte die Zeit ablaufen 
wird der Timer gestoppt und es erscheint eine Misserfolgsmeldung 
auf dem Bildschirm.

Bedienung:
----------

==================== ====================================================
Taste                Effekt
==================== ====================================================
0 bis 9              Entsprechende Ziffer in das Passwortfeld eingetragen
*Enter*              Password überprüfen
*Eingabetaste*       Password überprüfen
*Rücktaste*          Letzte Ziffer löschen
\-                   Letzte Ziffer löschen
*Leertaste*          Timer neu starten
*Links-Klick*        Timer neu starten
*Esc*                Programm verlassen
==================== ====================================================
