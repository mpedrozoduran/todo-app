filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    with(open(f"{filename}", 'r') as fh):
        print(fh.read())

