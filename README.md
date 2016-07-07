# pysnips

Pysnips is a compilation of useful python functions which all work in both Python2 and Python3. You can import the whole thing as a module, or just grab a specific method and use it directly in your code.




#### Make Table
Create a pretty and printable table of data from a list of dictionaries where the key in each dict is the header and the val is the column value
>INPUT: The `tabledata` argument is the list of dictionaries and the `columnorder` argument is an ordered list of how the columns should be displayed

>OUTPUT: The output of the method is a string of text which can be printed as an automatically formatted table.



#### Progress Bar
Print out an animated (but utterly useless) progress bar to the console which makes it look like your app is doing a bunch of important stuff in the background.
>INPUT: The "message" argument is a string used as the progress bar descriptor, the "seconds" argument is the number of seconds that the progress bar animation should last.

>OUTPUT: The printed output is animated and looks like: `<message>    [=================                ]`
