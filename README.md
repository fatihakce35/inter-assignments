# About program 
I made this program for my intern assignments. In this program, I used only built-in functions in python.

# How the filters work?

This program is designed to filter an okey game table based on the player's selected options.

The filtering method used in this program is based on the amount of the 'Bahis', whether the game is a 'rovans', whether it is 'hizi', and whether it is 'teke_tek'.

The 'rovans', 'hizi', and 'teke_tek' options all represent a binary number that corresponds to a 'Total' variable for the table.

For example:
rovans,  teke_tek,  hizli,
 0         0        0

These variables can be either 'yes' (1) or 'no' (0).

For instance, if we accept that the 'hizi' option is 'yes', the 'teke_tek' option is 'yes', and the 'rovans' option is 'no', we get the following table:

rovans, teke_tek, hizi
0          1      1

If we think of this table like binary numbers and convert it to a decimal, 4*0 + 2*1 + 1*1 = 3  we get a value of 3, which becomes our 'Total' value. We use this value along with the 'Bahis' value to filter the table!



