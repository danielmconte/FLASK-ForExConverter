### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
	1) Python tends toward the explict, while Javascript towards implicit.  So Python will throw errors when Javascript will throw undefined.
	2) Indentation in Python is necessary, while Javascript needs brackets and semi-colons.
	3) Python object is not a Javascript object (confusing), but Python dictionary is the equivalent to a Javascript object.  So while you can
	say nearly everything in both Javascript and Python are objects, that doesn't mean they are referring to the same thing.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

	1) dict.get("c") will return None, but you can pass in a second value to return if nothing is found
	2) You can use try/except

- What is a unit test?
>Small test, checking a single function or component

- What is an integration test?
>Medium-size test, checking how multiple functions or components interact

- What is the role of web application framework, like Flask?
>Flask handles the backend, specializing in making more concise syntax for common tasks such as routes.  In general frameworks are
extensive libraries making it easier to do common tasks.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
>The URL parameter is used for the subject, the material on the page. 
>The query string should be used as modifier (for example how to sort the page)

- How do you collect data from a URL placeholder parameter using Flask?
>Actually not entirely sure what this is specifically asking.

- How do you collect data from the query string using Flask?
>request.args[]
- How do you collect data from the body of the request using Flask?
>request.form[]
>request.data[]

- What is a cookie and what kinds of things are they commonly used for?
>Cookie serves as the memory for webpage. Commonly used for carts or advertisements 

- What is the session object in Flask?
>Sessions in Flask is built on top of cookies, so also serves as persistent memory each 'session' of the webpage.  
>Also, there is a thing called session storage that is larger than a cookie, but not the same at Sessions in Flask.	

- What does Flask's `jsonify()` do?
>Formats request responses into JSON. 
