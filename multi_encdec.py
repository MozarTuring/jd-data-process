from utils import str_concat

MAXSP = 5

ls_enc = []
ls_dec = []
with open('chat.nonewline', encoding='utf8') as rf:
  with open('chat.enc', 'w', encoding='utf8') as wf1:
    with open('chat.dec', 'w', encoding='utf8') as wf2:
      line = rf.readline()
      enc = ''
      dec = ''
      turn = 1
      switch = False
      count0 = False
      sessionID = '00029c51f92e8f34250d6af329c9a8df'
      t = 1
      while line:
        splitline = line.strip('\r\n').split(maxsplit=MAXSP)

        if splitline[0] == sessionID:
          if splitline[2] == '0':
            enc = str_concat(enc, splitline[-1])
            count0 = True
            if switch:
              ls_dec.append(dec)
              dec = ''
              turn += 2
              switch = False

          elif splitline[2] == '1' and count0:
            if not switch:
              ls_enc.append(enc)
              enc = ''
              switch = True
            dec = str_concat(dec, splitline[-1])

        else:
          sessionID = splitline[0]
          if dec:
            ls_dec.append(dec)
            dec = ''
          if enc:
            if len(ls_enc) < len(ls_dec):
              ls_enc.append(enc)
            enc = ''

#          if len(ls_dec) != len(ls_enc):
#            import ipdb
#            ipdb.set_trace()

          for en in ls_enc:
            en = en.replace('\t', '')
            wf1.write(en + '\t')
          wf1.write('\n')
          ls_enc = []

          for de in ls_dec:
            de = de.replace('\t', '')
            wf2.write(de + '\t')
          wf2.write('\n')
          ls_dec = []

          if splitline[2] == '0':
            enc = splitline[-1]
            count0 = True
            switch = False
            turn = 1
          else:
            dec = ''
            count0 = False
            switch = False
            turn = 1

        line = rf.readline()
        t += 1
        if t % 10000 == 0:
          print(t)

      print(t)
