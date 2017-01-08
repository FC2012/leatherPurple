#!/usr/bin/env python3 

import cgi 

form = cgi.FieldStorage()
text1 = form.getfirst ("TEXT_1" , "enter" )
text2 = form.getfirst("TEXT_2" , "outer" )


print ("Content-type: text/html\n")

print("""<!DOCTYPE html>
<head>
<meta carset="utf-8">
<title> FORM ADDING </title>
</head>
<body style="color:blue">
""") 
print("<p>TEXT_1: {}</p>".format(text1))

print("""</body>
</html>
""")

