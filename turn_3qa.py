from utils import str_concat

MAXSP = 5

def get_qa(ls1, ls2):
  qaqaq = ' '.join([ls1[0],ls2[0],ls1[1],ls2[1],ls1[2]]) 
  a = ls2[2]

  return qaqaq, a

if __name__ == '__main__':
  lls_enc = []
  lls_dec = []
  ls_enc = []
  ls_dec = []
  with open('chat.nonewline', 'r', encoding='utf8') as rf:
    with open('chat.enc', 'w', encoding='utf8') as wf1:
      with open('chat.dec', 'w', encoding='utf8') as wf2:
        line = rf.readline()
        enc = ''
        dec = ''
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

            assert len(ls_enc) == len(ls_dec)
            while len(ls_enc) >= 3:
              qaqaq, a = get_qa(ls_enc, ls_dec)
              del ls_enc[0]
              del ls_dec[0]
              wf1.write(qaqaq + '\n')
              wf2.write(a + '\n')

            if splitline[2] == '0':
              enc = splitline[-1]
              count0 = True
              switch = False
            else:
              dec = ''
              count0 = False
              switch = False

          line = rf.readline()
          t += 1
          if t % 10000 == 0:
            print(t)

        print(t)
