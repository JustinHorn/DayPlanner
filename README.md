![alt text](logo.jpg)

A project of mine that is supposed to help you plan your day. It is made for fast planning inside a .txt file.
## [Plan your day in 20s!](https://www.youtube.com/watch?v=idmiFDpcM0w)


# Why use DayPlanner for planning?
- save and reuse routines
- change duration easily
- calculates start and end for you
- insert activities you first forgot about easily
- navigate from one day to the next easily

# Layout
![alt text](tool.jpg)


# How to use it?


## Hotkeys

|use str & | meaning | what it does|
|---|---|---|
|enter|     enter|start next line with end time of old entry|
|n|     next|    increments time in small textiput|
|p|	    previous|   decrement time in small textinput|
|s|	    save|   saves current Template(routine) or Plan|
|l|	    load|   loads plan (name of plan = text in small textinput)|
|alt-gr|make routine|switches to routine mode with marked text|
|#|	        updateText|writes plan content to textinputs|
|spacebar| 	updatePlan|updates plan content by textiputs|


## Tutorial Video

[![Video explaining its use](http://img.youtube.com/vi/qoUj6SzII3w/0.jpg)](http://www.youtube.com/watch?v=qoUj6SzII3w)

# How does it work? 
The text that you enter is broken in to lines. Those lines are filtered acording to the following format:

^\d\d:\d\d activity

Lines that follow this format are entries. You can add a #command... and another \d\d:\d\d to the end of the entry.

The command will be ignored when comparing entries, it is used to make comannds without the programm forgetting the structure to the right. 

\d\d:\d\d at the end tells the program the duration of the activity eg. the length of the entry.

## Plan mode and Routine mode
You start in plan mode. Pressing on the Button that says "P/R" switches to routine mode. 

In routine mode you can change old routine or make new ones. Routine entries
are like plan entries except they have no start or end time they only have a duration. 

\d\d:\d\d stands for duration in this context

To create a new one change the theme in the small text input and save.
To change a old one click on it change it and save.
If there is a bugg when you swap to plan mode. Just save and restart the programm

# Get DayPlanner.exe via dropbox
[windows 64bit 7,8,10](https://www.dropbox.com/sh/ig1fnukoz3tq680/AACXfUxSOb_M0YYU1C5FDnBIa?dl=0)

# Why ?
I used to plan my days using vs-code and .txt files. I had to type in the same things over and over again. I wanted to automize that. Hence this project

# Credits
Thank you to all you tutorial makers on youtube and friends in my personal life. Without your guides and tipps all of this would have taken much longer.

# If you want to work on it yourself

The project uses [kivy](https://kivy.org/#home) and is based in a [conda](https://www.anaconda.com/) enviroment. 

