A REST api to be consumed by a mobile app, which is somewhat similar to various popular apps
which tell you if a number is spam, or allow  to find a person’s name by searching for their phone
number.

Data to be stored for each user:
● Name, Phone Number, Email Address.

Registration and Profile:
● A user has to register with at least name and phone number, along with a password, before
using. He can optionally add an email address.
● Only one user can register on the app with a particular phone number.
● A user needs to be logged in to do anything; there is no public access to anything.

Spam:
● A user should be able to mark a number as spam so that other users can identify spammers

Search:
● A user can search for a person by name in the global database. Search results display the name,
phone number and spam likelihood for each result matching that name completely or partially.
Results should first show people whose names start with the search query, and then people
whose names contain but don’t start with the search quer
