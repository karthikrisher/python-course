with open(r"F:\karthik\Data files\NIFTY_2018.csv", 'r') as fp:
    lines = sum(1 for line in fp)
    print('Total Number of lines:', lines)