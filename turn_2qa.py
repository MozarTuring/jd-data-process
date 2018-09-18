from utils import str_concat

if __name__ == '__main__':
  MAXSP = 5
  TURN = 3
  MIN_DEC = 4

  w_file1 = 'chat.enc'
  w_file2 = 'chat.dec'
  with open('chat.nonewline', encoding='utf8') as rf:
    with open(w_file1, 'w', encoding='utf8') as wf1:
      with open(w_file2, 'w', encoding='utf8') as wf2:
        line = rf.readline()
        enc = ''
        turn = 1
        switch = False
        count0 = False
        sessionID = '00029c51f92e8f34250d6af329c9a8df'
        t = 1
        while line:
          splitline = line.strip('\r\n').split(maxsplit=MAXSP)

          if splitline[0] == sessionID:
            if not flag:
              line = rf.readline()
              continue
              
            if turn == TURN:
              if splitline[2] == '1':
                # wf1.write(enc + '\n')
                turn = 1
                count0 = False
                # enc = '' 
                dec = splitline[-1]
                line = rf.readline()
                if line == '':
                  if len(dec) >= MIN_DEC:
                    wf1.write(enc + '\n')
                    enc = ''
                    wf2.write(dec + '\n')
                  break

                t += 1
                if t % 10000 == 0:
                  print(t)
                splitline = line.strip('\r\n').split(maxsplit=MAXSP)

                while splitline[2] == '1' and splitline[0] == sessionID:
                  dec = str_concat(dec, splitline[-1])
                  line = rf.readline()
                  t += 1
                  if t % 10000 == 0:
                    print(t)
                  if not line:
                    break
                  splitline = line.strip('\r\n').split(maxsplit=MAXSP)

                if len(dec) >= MIN_DEC:
                  #if len(dec) == MIN_DEC:
                  #  print(dec)
                  wf1.write(enc + '\n')
                  enc = ''
                  wf2.write(dec + '\n')
                  flag = False
                continue
              else:
                enc = enc + ' ' + splitline[-1]
                line = rf.readline()
                t += 1
                if t % 10000 == 0:
                  print(t)
                continue

            if splitline[2] == '0':
              enc = str_concat(enc, splitline[-1])
              count0 = True
              if switch:
                turn += 2
                switch = False

            elif splitline[2] == '1' and count0:
              switch = True
              enc = str_concat(enc, splitline[-1])

          else:
            sessionID = splitline[0]
            flag = True
            if splitline[2] == '0':
              enc = splitline[-1]
              count0 = True
              switch = False
              turn = 1
            else:
              enc = ''
              count0 = False
              switch = False
              turn = 1
              flag = False

          line = rf.readline()
          t += 1
          if t % 10000 == 0:
            print(t)

        print(t)
