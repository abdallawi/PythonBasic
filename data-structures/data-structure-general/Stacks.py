# Makes sense:

new_line = '\n'

# Lets make a list that mimics your browsing history, in order to learn about stacks.
# We will be using the LIFO principle: https://en.wikipedia.org/wiki/FIFO_and_LIFO_accounting#LIFO

history_browser = []  # just ignore the warning for learning purpose

# You can see this as a stack of information, that your browser holds for helping you navigate the interwebs
# So lets simulate a bit:

# User visits a few website:

history_browser.append('https://www.youtube.com/watch?v=P5hA0eT6it8')
history_browser.append('https://docs.google.com')
history_browser.append('https://www.imdb.com/title/tt2872732/?ref_=fn_al_tt_1')
history_browser.append('https://play.google.com')
history_browser.append('https://www.raspberrypi.org/')
history_browser.append('https://mail.google.com')
history_browser.append('https://netflix.com')

# Lets have a look what we already have in our browser history:
print(F'{"History Firefox:"} {history_browser}', new_line)

# The user pushes the back button:

last_website_visited = history_browser.pop()
print(F'{"Value taken out of browsing history:"} {last_website_visited}', new_line)

# Lets confirm that the website is taking out of our stack:
print(F'{"History Firefox:"} {history_browser}', new_line)

# But what happens if our user keeps pushing the back button:

history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()  # This one breaks it comment this line before going further

# Lets confirm that the websites are taking out of our stack:
print(F'{"History Firefox:"} {history_browser}', new_line)

# Remember Falsy values, lets use that to our advantage:

if not history_browser:  # Good practice!
    print('Trigger back button disable function')
