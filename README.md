# bowlingKata
python code for a bowling kata - Dient einer Übung in der 3 Lehrveranstaltung der ILV Software Testing

#Bowlingregeln
* Das Spiel besteht aus 10 Frames. In jedem Frame hat der Spieler zwei Würfe, um 10 Pins umzuwerfen. Die Punktzahl für den Frame ergibt sich aus der Gesamtzahl der umgeworfenen Pins, plus Boni für Strikes und Spares.
* Ein Spare ist, wenn der Spieler alle 10 Pins in zwei Würfen umwirft. Der Bonus für diesen Frame ist die Anzahl der Pins, die beim nächsten Wurf umgeworfen werden.
* Ein Strike liegt vor, wenn der Spieler alle 10 Pins mit seinem ersten Wurf umwirft. Der Frame wird dann mit einem einzigen Wurf abgeschlossen. Der Bonus für diesen Frame ist der Wert der nächsten beiden Würfe.
* Im zehnten Frame darf ein Spieler, der einen Spare oder Strike geworfen hat, die zusätzlichen Kugeln werfen, um den Frame abzuschließen. Es können jedoch nicht mehr als drei Kugeln im zehnten Frame geworfen werden.

#Aufgabe:
Schreibe Sie eine Klasse Game, die zwei Methoden hat
* void roll(int) wird jedes Mal aufgerufen, wenn der Spieler eine Kugel wirft. Das Argument ist die Anzahl der umgeworfenen Pins.
* int score() gibt die Gesamtpunktzahl für dieses Spiel zurück.

