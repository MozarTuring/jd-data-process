import codecs
with codecs.open('/mnt/dataset/finalTrainData/chat.txt','r',encoding='utf8') as rf:
  with codecs.open('chat.nonewline','w',encoding='utf8') as wf:
    line = rf.readline()
    line = rf.readline()
    print(line)
    t = 0
    while line:
      t += 1
      if t % 10000 == 0:
        print(t)
      if line != '\n':
        if line.endswith('\n'):
          wf.write(line)
        else:
          wf.write(line[:-1])

      line = rf.readline()

