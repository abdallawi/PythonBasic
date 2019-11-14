from collections import deque

kenan = 'Kenan'
bart = 'Bart'
wouter = 'Wouter'
patrick = 'Patrick'
noureyne = 'Noureyne'
alex = 'Alex'
fares = 'Fares'
rania = 'Rania'
joke = 'Joka'

waiting_queue = deque([])

waiting_queue.append(kenan)
waiting_queue.append(bart)
waiting_queue.append(wouter)
waiting_queue.append(patrick)
waiting_queue.append(noureyne)
waiting_queue.append(alex)
waiting_queue.append(fares)
waiting_queue.append(rania)
waiting_queue.append(joke)

print(f'Waiting line: {waiting_queue}')

for person in range(len(waiting_queue)):
    print(f'Served: {waiting_queue.popleft()}', '\n')
    print(f'Waiting line: {waiting_queue}', '\n')
else:
    print("All is done")
