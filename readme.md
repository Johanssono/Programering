Logbok
==============


Vecka 16
--------------
Jag har jobbat med att få så att man altid har alternativet att välja chans tills man valt det. Jag har även börjat kolla på hur jag ska göra för att göra det möjligt för fler personer att spela samtidigt och emmot varandra.

Nästa gång ska jag dock börja jobba på strukturen med och fökusera på att förkorta och omvandla kod som upprepar sig till slingor eller liknande.

Vecka 15
--------------
Jag har ändrat min kod och har gjort så att jag räknar antalet av varge siffra i listan med tärningarna med hjälp av dice.count(a), om det finns fler av ett tal än 1, till exempel om det finns två eller fler fyror i listan, så tas dessa bort och läggs in i en ny lista. Denna nya listan avgör om man kan välja mellan kåk eller liknande genom att avgöra hur lång den nya listan är. Om den nya listan är 3 objekt lång vet jag att det bara kan finnas tre av en siffra då det inte kan vara en ensamn siffra i listan. om det finns fyra kan det antingen vara fyra av en eller kåk, detta avgör jag genom att räkna antalet av av varge siffra i den nya listan och om gör igentligen om prosessen en gång till.

Detta gör att min kod inte blir jätte snygg dock.

Jag har inte hunnit testa om det fungerar utan behöver göra det nästa gång.

källor för dagens problem är Rikard då han gav mig tipset på att använda dice.count(a)

Jag har nu kollat och fixat så att koden fungerar och ger spelaren rätt alternativ. Koden kan avgöra om spelaren ska få alternativ som två par eller par eller båda baserat på längden av listan "par" och om första och sista siffran i listan är samma.

Jag ska nu börja jobba på att göra så man kan spela fler personer och lägga in sina poäng i poänglistor så att man kan spara sina poäng per spelare.

Vecka 14
--------------
lov


Vecka 13
--------------
Jag kollat in på att använda mid av count för att räkna ut hur många av varge tal som finns i listan och om ett tal upprepas mer än en gång och mindre än fyra gånger, ska detta talet dubblas och läggas in i listan tvåpar för att äkna ut om det finns två stycken par i listan med tärningar. Men jag vet inte hur jag ska göra för att koden inte ska räkna båda femmorna två gånger.

Jag använde mig av denna hemsidan: https://docs.python.org/3/tutorial/datastructures.html

Vecka 12
--------------
Jag har skapat en kod som ska kolla om spelaren har möjlighet att med sina tärningar välja saker som "tvåpar" och "kåk". Jag har inte hunnit jobba så mycket med koden och det är bara ett test för att kolla om jag kan göra som jag tänker mig och funkar inte riktigt än. Jag har inte hunnit testa koden ordentligt och behöver fortsätta med den nästa vecka.

Jag har trixat och exprementerat med olika versioner av koden jag vill skapa men har inte kommit fram till en passande version än, ska fortsätta med detta.

Jag testade även en kod som tog fram indexet för andra upprepningen av ett tal i listan, dvs att om en lista hade mer än en av siffran 5 skulle koden ta fram indexet för den andra 5,an. Detta fungerade så länge inte båda femmorna är brevid varandra i listan.

För den här koden använde jag mig av den här hemsidan: https://www.reddit.com/r/learnpython/comments/tedz22/second_occurrence_index_number_from_list/?rdt=46815&onetap_auto=true&one_tap=true

Vecka 11
--------------

*Torsdag*: Jag har fixat så att koden bara ger en ett alternativ av valmöjligheter oavsätt om man har, till exempel, om man har flera ettor så får man ändå bara alternativet att välja ettor en gång istället för tidigare då man fick alternativet lika många gånger som mängden ettor man har. 

Jag kom på att jag kan skapa en kod som använder sig av en variabel. Denna variabel ska ta värdet av objektet i index 1 i listan med tärningar och sedan räkna hur många gånger detta värdet finns i listan, till exempel om index 1 = 2 ska variabeln ta värdet 2 och kolla hur många tvåor som finns i listan. Sedan ska koden upprepa detta för alla index i listan och på något sätt hoppa över index som har samma värde som ett index som redan räknats. Men jag han inte börja utan ska försöka komma på hur denna koden ska se ut nästa lektion.



Koden jag skrev förra veckan fungerade lita halvt och började om utan spelarens godkännande, detta var jobbigt då det var småproblem inne i koden som påverkade. Jag löste detta genom att ändra värdet på variabeln "kasta" så att while loopen inte upprepar sig, sedan ändrade jag så att man inte får alternativet att spara tärningar sista kastet då alla tärningar ändå ska sparas. 

Jag gjorde även att när man spelat klart en omgång och valt vart poängen ska placeras så kan man välja att spela igen.

Dett uppstod dock ett problem med koden, när man ska välja vart man vill lägga poängen så upprepade den alternativen för varge siffra som upprepades mer än en gång, så om man hade tärningarna "2,3,4,5,5" skulle alternativet för att lägga poängen på "femmor" upprepas två gånger.
Jag han dock inte kolla på att fixa detta problemet, utan får göra det nästa gång.

Jag han även inte kolla på hur jag skulle lösa att ge alternativ för "kåk" eller liknande, så just nu kan man bara lägga poängen på 1-6. Jag han även inte riktigt kolla om koden som genererar listan med poäng alternativ fungerar till 100%, utan han bara kolla så att den fungerar i stort sätt.

Nästa gång ska jag kolla närmare på koden som genererar poäng alternativen och upprepningen av alternativ. Om jag hinner ska jag även kolla på om jag kan hoppa över frågan om man vill redigera listan med sparade tärningar om man inte har några sparade tärningar.

Vecka 10
--------------
Jag har skapat en kod som teoretiskt kollar igenom tärningarna och kollar om det finns tillgängliga alternativ mellan 1-6 som spelaren kan ta. sedan visar koden spelaren listan med tillgängliga alternativ och låter spelaren välja vart poängen ska läggas. Sedan läggs alla poäng i en lista fr det specifika valet och summeras.

nästa gång ska jag testa att koden och även förbätttra systemet. Sedan ska jag komma på ett sätt att avgöra om spelaren med sina träningar kan välja mer speciella poängalternativ som kåk och stege.

Jag ska även fixa så att man alltid sparar alla träningar vid sista kastet.

Koden är i en evighets loop då den alltid frågar om man vill kasta tärningarna och sedan börjag om, ska kolla in på detta

https://www.w3schools.com/python/python_operators.asp
https://www.markdownguide.org/cheat-sheet/

Jag använde dessa två länkar för att kolla hur man gjorde \n respektive lista i markdown.

Lista
--------------
-Jag ska skapa en kod som söker ut vilka poäng alternativ man har möjligheten att välja och sedan spara poängen i valt alternativ.
-Jag ska skriva en kod som låter en välja ett poäng alternativ att stryka om det inte finns alternativ att välja mellan som passar ens tärningar.
-Jag ska fixa så koden visar summan av alla poäng och resultatet av spelet.
-Jag ska eventuellt även fixa så att man kan spela flera spelare.

Vecka 9
--------------
Jag bollade med vikarien och kom fram till att jag kan skapa ett programm som utifrån innehållet på listan med tärningar, kollar vilka kriterier som tärningarna uppfyller och ger sedan spelaren alternativen som spelaren kan lägga poängen på, till exempel 2 par eller kåk. Jag ska sedan skriva ett program som kollar vilka poäng som spelaren får beroende på vart hen väljer att lägga poängen och sedan tar bort detta alternativet så att spelaren inte kan lägga poängen där igen. Detta ska jag sedan modifiera så att flera spelare kan spela.

jag måste även skriva en kod som tar bort ett alternativ om spelarens tärningar inte uppfyller några krav.

Men jag ska snacka med Rickard om han tycker att jag ska göra det objektorienterat eller om jag även kan få A utan.


Vecka 8
--------------
Jag jobbade med att förska lära mig objekt orienterad programering och ska fortsätta med detta.

vecka 6
--------------
Jag han inte så mycket denna veckan då vi gjorde scratch och jag satt och bollade ideer mer Ronnie hur jag ska göra med tabellen nästa gång.

vecka 5
--------------
Denna veckan övade vi på scratch.

vecka 4
--------------
Jag har fixat så att funktionen (for i in range(len(dice) -1, -1, -1):) kan analysera alla tärningar i listan, detta gjorde jag genom att ändra funktionen från for i in range(len(dice) -1, 0, -1): till for i in range(len(dice) -1, -1, -1):. Ändringen av värdet 0 till 1 gör att funktionen räknar listan från index värde -1 och går ned med 1 steg fram till index -1, vilket gör att den även analyserar index 0 vilket den hopade innan.

Jag har dock fått problem med att funktionen while kast > 0: inte fungerar och gör så att spelare kan kasta hur många gånger som hällst. detta borde vara ett lätt problem att lösa men hade inte tid, det får bli till nästa gång. 

Jag ska snart börja på poängsystemet som är i yatzy.

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

