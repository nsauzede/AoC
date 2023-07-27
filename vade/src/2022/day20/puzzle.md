\--- Day 20: Grove Positioning System ---
----------

It's finally time to meet back up with the Elves. When you try to contact them, however, you get no reply. Perhaps you're out of range?

You know they're headed to the grove where the *star* fruit grows, so if you can figure out where that is, you should be able to meet back up with them.

Fortunately, your handheld device has a file (your puzzle input) that contains the grove's coordinates! Unfortunately, the file is *encrypted* - just in case the device were to fall into the wrong hands.

Maybe you can decrypt it?

When you were still back at the camp, you overheard some Elves talking about coordinate file encryption. The main operation involved in decrypting the file is called *mixing*.

The encrypted file is a list of numbers. To *mix* the file, move each number forward or backward in the file a number of positions equal to the value of the number being moved. The list is *circular*, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.

For example, to move the `1` in a sequence like `4, 5, 6, *1*, 7, 8, 9`, the `1` moves one position forward: `4, 5, 6, 7, *1*, 8, 9`. To move the `-2` in a sequence like `4, *-2*, 5, 6, 7, 8, 9`, the `-2` moves two positions backward, wrapping around: `4, 5, 6, 7, 8, *-2*, 9`.

The numbers should be moved *in the order they originally appear* in the encrypted file. Numbers moving around during the mixing process do not change the order in which the numbers are moved.

Consider this encrypted file:

```
1
2
-3
3
-2
0
4

```

Mixing this file proceeds as follows:

```
Initial arrangement:
1, 2, -3, 3, -2, 0, 4

1 moves between 2 and -3:
2, 1, -3, 3, -2, 0, 4

2 moves between -3 and 3:
1, -3, 2, 3, -2, 0, 4

-3 moves between -2 and 0:
1, 2, 3, -2, -3, 0, 4

3 moves between 0 and 4:
1, 2, -2, -3, 0, 3, 4

-2 moves between 4 and 1:
1, 2, -3, 0, 3, 4, -2

0 does not move:
1, 2, -3, 0, 3, 4, -2

4 moves between -3 and 0:
1, 2, -3, 4, 0, 3, -2

```

Then, the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value `0`, wrapping around the list as necessary. In the above example, the 1000th number after `0` is `*4*`, the 2000th is `*-3*`, and the 3000th is `*2*`; adding these together produces `*3*`.

Mix your encrypted file exactly once. *What is the sum of the three numbers that form the grove coordinates?*

To begin, [get your puzzle input](20/input).

Answer:

You can also [Shareon [Twitter](https://twitter.com/intent/tweet?text=%22Grove+Positioning+System%22+%2D+Day+20+%2D+Advent+of+Code+2022&url=https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F20&related=ericwastl&hashtags=AdventOfCode) [Mastodon](javascript:void(0);)] this puzzle.ave 2 ore.
1 clay-collecting robot collects 1 clay; you now have 1 clay.

== Minute 5 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
1 clay-collecting robot collects 1 clay; you now have 2 clay.
The new clay-collecting robot is ready; you now have 2 of them.

== Minute 6 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
2 clay-collecting robots collect 2 clay; you now have 4 clay.

== Minute 7 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
2 clay-collecting robots collect 2 clay; you now have 6 clay.
The new clay-collecting robot is ready; you now have 3 of them.

== Minute 8 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 9 clay.

== Minute 9 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
3 clay-collecting robots collect 3 clay; you now have 12 clay.

== Minute 10 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
3 clay-collecting robots collect 3 clay; you now have 15 clay.

== Minute 11 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 4 clay.
The new obsidian-collecting robot is ready; you now have 1 of them.

== Minute 12 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
3 clay-collecting robots collect 3 clay; you now have 7 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
The new clay-collecting robot is ready; you now have 4 of them.

== Minute 13 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 11 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.

== Minute 14 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 15 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.

== Minute 15 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
4 clay-collecting robots collect 4 clay; you now have 5 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
The new obsidian-collecting robot is ready; you now have 2 of them.

== Minute 16 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 9 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.

== Minute 17 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 13 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.

== Minute 18 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 17 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
The new geode-cracking robot is ready; you now have 1 of them.

== Minute 19 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 21 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 1 open geode.

== Minute 20 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 25 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.

== Minute 21 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 29 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
The new geode-cracking robot is ready; you now have 2 of them.

== Minute 22 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 33 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.

== Minute 23 ==
1 ore-collecting robot collects 1 ore; you now have 5 ore.
4 clay-collecting robots collect 4 clay; you now have 37 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.

== Minute 24 ==
1 ore-collecting robot collects 1 ore; you now have 6 ore.
4 clay-collecting robots collect 4 clay; you now have 41 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.

```

However, by using blueprint 2 in the example above, you could do even better: the largest number of geodes you could open in 24 minutes is `*12*`.

Determine the *quality level* of each blueprint by *multiplying that blueprint's ID number* with the largest number of geodes that can be opened in 24 minutes using that blueprint. In this example, the first blueprint has ID 1 and can open 9 geodes, so its quality level is `*9*`. The second blueprint has ID 2 and can open 12 geodes, so its quality level is `*24*`. Finally, if you *add up the quality levels* of all of the blueprints in the list, you get `*33*`.

Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. *What do you get if you add up the quality level of all of the blueprints in your list?*

To begin, [get your puzzle input](19/input).

Answer:

You can also [Shareon [Twitter](https://twitter.com/intent/tweet?text=%22Not+Enough+Minerals%22+%2D+Day+19+%2D+Advent+of+Code+2022&url=https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F19&related=ericwastl&hashtags=AdventOfCode) [Mastodon](javascript:void(0);)] this puzzle.