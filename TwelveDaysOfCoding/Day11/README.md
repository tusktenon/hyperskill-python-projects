# On The Eleventh Day Of Coding...

[View on Hyperskill](https://hyperskill.org/learn/daily/53352)

*On the eleventh day of coding my team lead sent to me... Eleven baked bakers,*

*Ten little drummers, nine cat lives, eight queens, seven Bridges of Königsberg,*

*Six handshakes, five-pointed star, four dining elves, three security rules, two pointers, and a nasty bug in a production tree!*

You find Mr. Frost in the office's bakery. "Look what's happening here. Our eleven gingerbread workers need to bake various cookies. But it's not that straightforward. You can't frost cookies before you've baked them, and you can't make sandwich cookies before both halves are ready. So some actions must be done before the others are performed. Surely you understand how complex baking can really get."

He hands you a production schedule. "Here. Each baking action has a duration and a list of which actions must be completed first. Up to eleven gingerbread people can work in parallel on independent baking actions, but an action can only start once ALL its dependencies are done. We need this done by lunch. Can you tell me how much time will it approximately take? We need to hurry up, so don't waste your time calculating it down to a second, an answer using critical path schedule will be good enough. They teach kids outside the North Pole about that, right?"

**Input format:** One action per line: `action_id,duration,dependencies`

- **action_id:** Unique identifier (0, 1, 2, ...)
- **duration:** Minutes to complete this action
- **dependencies:** Colon-separated list of actions IDs that must finish first, or `none` if no dependencies

**Example:** `5,20,2:3` means action 5 takes 20 minutes and requires actions 2 and 3 to be done first.
**Output:** Minimum time in minutes to complete all actions with 11 workers working in parallel.

**Hint:** You might want to read about [Directed acyclic graphs](https://hyperskill.org/learn/step/21386) first.

> [!IMPORTANT]
> Don't try to bruteforce this task. Computing true minimum might take surprisingly longer than you think (complexity is exponential).
>
> Also, Mr. Frost will specifically accept only an answer calculated using [Critical Path](https://en.wikipedia.org/wiki/Critical_path_method) Scheduling (also known as [List Scheduling](https://en.wikipedia.org/wiki/List_scheduling) with critical path priority) - which respects both task dependencies AND the 11-worker limit. At each time step, among all tasks whose dependencies are complete, prioritize scheduling those on the critical path first (tasks that would delay the overall completion if delayed).

***NOTE:*** I also found the following links quite helpful for determining the critical path:

- [Critical Path Method for Project management](https://www.geeksforgeeks.org/project-mgmt/software-engineering-critical-path-method/)
- [Critical Path Analysis: A How-to Guide (with Example)](https://www.projectmanager.com/blog/critical-path-analysis-example-template)
