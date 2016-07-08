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



#### Status Reporter
Report on standard status messages coming from other input check functions in pysnips. The status reporter is built around a standard messaging format in pysnips which is defined below.

**Messaging Standard**
* A standard status message from a "check" method is dictionary formatted as `{'status': <pass, warning, or fail>, 'messages': [<list of dicts>]}`
* The 'messages' value is a list of dicts. Each dict in the list is formatted as `{<OK, WARNING, or FATAL>: <Readable message from the specific check>}`

**Status Reporter Details**

>INPUT: Input argument "statusdata" is a standard check message as defined in the "Messaging Standard" section.

>INPUT: Input argument "reportlevel" can have values (onfail | onwarning | all) which set the level of report by the function

>OUTPUT: Output is a string of prinatable status messages which report on the different checks



#### Check Domain Name
Check a domain or FQDN host name for legitimacy and proper formatting.
>INPUT: Input "domainname" is a string of the domain name

>OUTPUT: Output will be a pass/fail with status messages formatted in the standard messaging format (see "Status Reporter" for more info)
