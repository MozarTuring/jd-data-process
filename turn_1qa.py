from utils import str_concat

if __name__ == '__main__':
  MAXSP = 5

  w_file1 = 'chat.turn_1st.enc'
  w_file2 = 'chat.turn_1st.dec'
  with open('chat.nonewline', encoding='utf8') as rf:
    with open(w_file1, 'w', encoding='utf8') as wf1:
      with open(w_file2, 'w', encoding='utf8') as wf2:
        line = rf.readline()
        sessionID = None
        t = 1
        while line:
          splitline = line.strip('\r\n').split(maxsplit=MAXSP)
          
          if splitline[0] == sessionID:
            if not flag:
              line = rf.readline()
              continue
            else:
              if splitline[2] == '0':
                enc = str_concat(enc, splitline[-1])
  
              else:
                dec = splitline[-1]
                line = rf.readline()
                if line == '':
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
  
                wf1.write(enc + '\n')
                enc = ''
                wf2.write(dec + '\n')
                flag = False
                continue

          else:
            sessionID = splitline[0]
            if splitline[2] == '0':
              enc = splitline[-1]
              flag = True
            else:
              flag = False
              line = rf.readline()

          line = rf.readline()
          t += 1
          if t % 10000 == 0:
            print(t)

        print(t)
