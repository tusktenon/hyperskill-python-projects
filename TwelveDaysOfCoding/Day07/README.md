# On The Seventh Day Of Coding...

[View on Hyperskill](https://hyperskill.org/learn/daily/53348)

*On the seventh day of coding my team lead sent to me... Seven Bridges of Königsberg,*

*Six handshakes, five-pointed star, four dining elves, three security rules, two pointers, and a nasty bug in a production tree!*

Mr. Frost walks in carrying a historical map. "Have you heard of the Seven Bridges of Königsberg? It's one of the most famous problems in mathematics. The city had seven bridges, and people wondered if you could walk a path crossing each bridge exactly once."

He pulls up a modern map on his screen showing a complex network of land masses connected by 700 bridges. "We have a similar problem here at the North Pole - our transportation network has grown massive. I need to know: can our delivery routes cross each bridge exactly once? And if not, what's the MINIMUM number of times we have to go through a bridge we have already visited to cover all bridges in our network?"

**Input format:** List of landmasses connected by bridges, one per line in format `LandMass1,LandMass2` (remember that bridges are bidirectional).
**Output:** The minimum number of additional bridge crossings required (beyond crossing each bridge once). Or 0 if it's possible to cross each bridge exactly once.
**Hint:** You might want to read about [Eulerian paths](https://en.wikipedia.org/wiki/Eulerian_path) if you are not yet familiar with it.
