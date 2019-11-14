new_line ='\n'

history_browser = []

history_browser.append('https://www.youtube.com/watch?v=P5hA0eT6it8')
history_browser.append('https://docs.google.com')
history_browser.append('https://www.imdb.com/title/tt2872732/?ref_=fn_al_tt_1')
history_browser.append('https://play.google.com')
history_browser.append('https://www.raspberrypi.org/')
history_browser.append('https://mail.google.com')
history_browser.append('https://netflix.com')

print(history_browser)

last_visited_website = history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()
history_browser.pop()

print(history_browser)

if not history_browser:
    print('the forward button is disabled')
else:
    print()
    history_browser.pop()
