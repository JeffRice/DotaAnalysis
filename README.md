# DotaAnalysis
DoTa 2 data analysis

This is a collection of scripts that queries the Dota2 Web API and performs some operations on that data. I am interested in 
obtaining and storing match details to run data analysis on the results.

It works by getting match ID's of recent games in groups of 100. Then each of these ID's is used to retrieve match details about 
that particular game. I do some checking to see if it's a game I want to keep. There are many game modes and reasons to not store 
the data (people leaving the game, maybe it's a game against bots and not even real people). It checks for all these factors and 
then throws out the games for results we don't want.

The Steam web API uses integers wherever possible to save space, so I do some conversion of values and format them in a usable way. 
Then they are stored in a mongoDB database. The particular information I am looking for in these analyses is what heroes work well 
in combination with other heroes as partners and how effective they are against certain opponents and teams. The game match details 
can then be queried from the mongoDB to gain insight into these trends using the latest match details! 
