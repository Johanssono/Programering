Logbok
==============

vecka 3
--------------
Jag satt och jobbade skoningslöst med min kod för att lösa ett specifikt problem med while-slingan som skulle ta bort de sparade tärningarna från listan. Om två ombjekt som skulle tas bort var direkt efter varandra hopade for-slingan över det andra objektet då den fick samma ett nytt index som var samma som den som precis togs bort. Sedan råkade en olycka hända som tog bort all den kod jag skrivit på lektionen, men jag skrev snabbt tillbacka koden då jag viste hur det skulle se ut och sedan hjälpte rickard mig att vända på for-slingan som skulle ta bort objekt så inga objekt byter index.

Jag fixade problemet med att låta spelaren spara flera olika tärningar och sedan gjorde jag så att dem tärningar som inte sparades kastades om och sedan får spelaren välja igen mellan de nya tärningarna och dem som spelaren sparade föra kastet. Jag gjorde även så att spelaren kan välja att ta bort tärningar från dem hen sparade och kasta om dem. Spelaren kan reperera allt detta i tre kast.

Nästa gång kan jag nog börja fixa med att göra så att spelaren kan lägga in dem sparade tärningarna i ett poängsystem och stryka saker om dem misslyckas.

vecka 2
--------------
Jag jobbade med att försöka sätta mig in i arbetet igen. Jag hade problemet att när jag skulle spara tärningar och ta bort de tärningar som inte skulle sparas, hoppar listan över det andra talet om två tal som ska bort är direkt efter varandra. Jag googlade men hittade ingen smidig lösning på problemet, tills jag kom på att jag kan ta bort listan med sparade tärningar och endast göra så att de tärningar som ska bort försvinner. Jag fixade även med hur man skulle ta bort tärningar om man ville och sedan kasta om tärningarna. Nu tror jag att allting fungerar som det ska men måste testa nästa gång om koden fungerar när man kastar 3 gånger i rad då jag inte han det denna veckan.

vecka 51
--------------
Jag fixade med while loopen som skulle låta spelaren kasta tärningarna 3 gånger och spara dem i olika listor, behöver fortsätta jobba med den nästa gång och behöver fixa så att spelaren kan ta bort saker från listan med sparade tärningar och spara olika kombinatniner av tärningar så som stege/kåk. Det var svårt att lyckas fixa while loopen så att den fungerar utan att använda en onödigt stor mängd kod.

vecka 50
--------------
Jag har nu skrivit en kod som skapar en spelare och kastar tärningar, jag ska dock ändra nästa gång hur programmet frågar vilka träningar som ska sparas och sedan göra om koden som kastar de soparade tärningar då det hamnade i en evighets loop. Det var rätt svårt att få en idée och komma igång med hur man ska göra men mycket enklare när man väl började.

vecka 49
--------------
Jag hade inte fixat allting med min nya skoldator och var tvungen att lägga hela lektionen på att ladda ner vs codium och annat för att få allting att fungera. Jag lyckades med prov 10, skrivit en lista på vad jag ska göra och pratade ideer med Rickard, jag ska kolla på dictionaries nästa gång.

0. Jag ska skapa en kod där en spelare kan spela yatzy.
0. Jag ska göra så att programet har koll på vilka tärningar som spelaren väljer att spara vid varge kast.
0. Jag ska göra så att programet har koll på vilka saker som spelaren fått poäng i och vilka saker som är strukna
0. skapa så att programmet frågar vilka siffror som spelaren vill spara och att spelaren akn skriva in flera värden avskillda av ett mellanrumm som svar till frågan ( använd lista till detta)


vecka 48
--------------
Jag började med att skriva kod till ett Jatzy, jag lyckades inte komma så långt, utan lyckades bara göra en kod för att skriva in hur många spelare som ska spela och sedan vad dessa spelare ska heta. Nästa gång får jag nog läsa mig in på klasser för att kunna gå vidar med uppgiften.


Kolla på vecka 48 och framåt för eget programerings projekt
==============

vecka 47
--------------
Jag har börjat jobba med dictionary och har börjat med en kod där man skriver in ett ord på valfritt språk och sedan en översättning av det ordet på svenska, om först ordet man skrev in var på svenska får man välja valfritt språk på andra ordet. Jag vet dock inte riktigt hur jag ska göra för att få in det i en fungerande loop, men det borde vara lätt löst nästa gång.

vecka 46
--------------
Jag har gjort färdigt min kod med olika konverterare och har nu börjat arbeta på en kod som ska översätta text till rövarspråket. Om tid och ork finns vill jag även göra så att man kan översätta rövarspråket till vanlig text.

Jag vet dock inte riktigt hur jag ska få koden att kolla om bokstäverna i ett ord matchar listan med konsonanter och sedan lägga till den röverfierade varianten i "rövar_svar" om bokstaven är en konsonant.

Jag gjorde prov 8 och 9, sedan fortsatte jag med koden "rovarspråket". Jag förstog hur jag skulle göra men gjorde lite små fel, jag skrev exempelvis "rovar_svar" som en lisa i funktionen när det bara var string i koden. Jag hade även lite problem med att förstå hur den skulle kolla om bokstaven fanns i min lista "konsonanter", men det löste jag snabbt genom att ändra "if i == konsonanter" till "if i in konsonanter"

Vecka 45
--------------
Jag har jobbat med listor och deffinitioner i mapp 7080. Jag gjord inte så mycket mer än att testa runk och försöka förstå hur det fungerade, men verkar kunna det nu. Jag har även börjat att arbeta med en kod som låter en välja mellan vilka enheter man vill konvertera mellan men han inte klart med att få det och fungera. Jag har även använt mig av väldigt många "if"/"elif" för att skapa koden och ska nästa gång kolla om jag kan göra det snyggare på ett annat sätt. men den är som sagt inte klar.

Jag har fortsatt med arbetet på min kenvertetringskod men lyckades inte komma så långt, jag fastnade i att omvandla formeln från celcius till farenhight så att den gick åt andra hållet. Jag kom därför ingnstans idag.

Vecka 44
--------------
LOV

Vecka 43
--------------
Jag övade lite inför prov 7 och testade koderna till provet, sedan skulle jag texta att kolla på uppgiften (printa alla primtal upp till 100) i uppgift 7100. Men jag förstod inte hur jag skulle göra. Jag googlade men hittade inte direkt ett sätt att börja. Jag googlade sedan upp ett svar för att försöka förså hur koden fungerade då koden använde sig av funktioner jag inte använt än. Hittade koden på: https://stackoverflow.com/questions/15963707/python-displays-all-of-the-prime-numbers-from-1-through-100. Jag gick sedan igenom koden med Rikard för att förstå hur den fungerar och tror jag gör det nu. Jag lärde mig lite om hur man använder "true" och "false". Skulle vilja testa om jag kan lösa det nästa gång med vad jag har lärt mig idag.

Vecka 42
--------------
Jag skrev en kod som kastade 10 tärningar och sparade dessa värden i en lista, uppgift 7100. Sedan presenterade koden största/minsta värde, summan, medelvärdet, hur många sexor och vilket tal som var vanligast. Använde mig först av listor för att få ut det vanligaste talet, deta skrev dock inte ut vilket som var det vanligaste men istället hur många av det vanligast som slogs. Jag ska därför försöka göra på ett annat mer kompremerat sätt för att få det resultat jag vill ha.

Jag upptäckte att min kod inte skriver vilket tal som är vanligast utan hur många det var av dem. Jag fick nu förklarat för mid hur koden Rikard skrev fungerar och det löser mitt problem. Med hjälp av Rikards kod skapade jag en liten egen kod med lite skillnader från rikads kod, detta så att den fungerar till den långa koden jag skrev för att räkna ut största talet.

Jag lärde mig att hur jag ska använda listor mer effektivt och lite djupare om hur listor fungerar

Vecka 41
--------------
Jag lekte runt lite med listor Och städat i andra koder. Jag gjorde lite övningar med alla kommandon. Jag glömde doch vad mer jag gjorde och glömde skriva ner det.

Vecka 40
--------------
Jag jobbade med med "for", byde 7095 och 7096. Detta var enkelt och jag stötte inte på några svårigheter. Jag undrade dock varför man var tvungen att använda sig av srt och liknande, men fick frågat det på lektionen och förstår varför.

Vecka 39
--------------
Jag fixade klart, men hadde problem med att v1 inte körde oändligt utan printade bara "sten,sax,påse" om och om igen. Fixade detta genom att ändra while while "svar == "j" or "ja":" till while "svar == "j" or svar == "ja":" och "if svar == "j" or "ja":" till "if svar == "j" or svar == "ja":"

Jag gjorde sedan en omvandling på ett litet flödesdiagram till kod utan svårigheter.

Vecka 38
--------------
Jag jobbade med mitt sten, sax, påse spel men fick inte programmet att fungera med random.choice funktionen då jag inte visste att jag inte kunde kombinera print och input. Men medans jag försökte lösa problemet testade jag att göra samma spel fast använda mig av random nummer istället. detta fungerade direkt och jag kunde tyvär inte lista ut vad problemet med det första var förän jag frågade Rikard i slutet av lektionen och han påpekade att input inte "ger någonting tillbaka".

