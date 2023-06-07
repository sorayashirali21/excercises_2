#pr 4

file_path = 'email-Eu-core.txt'

def count_source_sink_isolated_nodes(file_path):
    receivers = set()
    sources = set()
    senders = set()
    sinks = set()

    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            receivers.add(receiver)
            senders.add(sender)
            sources.discard(receiver)
            sources.add(sender)
            sinks.discard(sender)
            sinks.add(receiver)

    num_source_nodes = len(sources)
    num_sink_nodes = len(sinks)
    isolated_nodes = senders.symmetric_difference(receivers)
    num_isolated_nodes = len(isolated_nodes)
    return num_source_nodes, num_sink_nodes, num_isolated_nodes

num_source_nodes, num_sink_nodes, num_isolated_nodes = count_source_sink_isolated_nodes(file_path)
print('Result Question 4: ')
print('Number of sources nodes:', num_source_nodes)

#===============================================
'''output pr 4:
تعداد گره های منبع: 396
تعداد گره های پایانی: 644
تعداد گره های ایزوله: 151
'''