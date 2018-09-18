import re
MIN_COUNT_ENC = 0
MIN_COUNT_DEC = 0

START_VOCAB =['<unk>', '<s>', '</s>']
EXCLUDE_LS = ['', '\n']
RE_DIGIT = re.compile('\d')


def file2vocab(rfile, vocab):
  print('start creating vocabulary from %s' % (rfile))
  with open(rfile, 'r', encoding='utf-8') as rf:
    line = rf.readline()
    t = 0
    while line:
  #        wf.write(line)
      t += 1
      if t % 10000 == 0:
        print(t)
      ls_line = line.split()
      for li in ls_line:
        if li in EXCLUDE_LS:
          continue
        if li not in vocab:
          vocab[li] = 1
        else:
          vocab[li] += 1

      line = rf.readline()
  print('done')

def write_vocab(wfile, vocab, ls_vocab):
  print('writing vocabulary to %s' % (wfile))
  with open(wfile, 'w', encoding='utf-8') as wf:
    for vo in START_VOCAB:
      wf.write(vo + '\n')
    for vo in ls_vocab:
      wf.write(vo + '\n')
      if vocab[vo] == MIN_COUNT:
        break
  print('done')

def create_vocab(**kwargs):
  vocab = {}
#  wf = codecs.open(kwargs['wfile'], 'w', encoding='utf-8')
  if len(kwargs) >= 2:
    rfile1 = kwargs['rfile1']
    file2vocab(rfile1, vocab)
  if len(kwargs) >= 3:
    rfile2 = kwargs['rfile2']
    file2vocab(rfile2, vocab)

  ls_vocab =  sorted(vocab, key=vocab.get, reverse=True)
  
  wfile = kwargs['wfile']
  write_vocab(wfile, vocab, ls_vocab)
#  tt = 0
#  for kk, vv in vocab:
#    if vv >= MIN_COUNT:
#      tt += 1
#
#  print('%d words appear at least %d times' % (tt, MIN_COUNT))


if __name__ == '__main__':
  split_dir = 'jieba_split/'
  suffix = '.dec'
  if suffix == '.dec':
    MIN_COUNT = MIN_COUNT_DEC
  if suffix == '.enc':
    MIN_COUNT = MIN_COUNT_ENC
  read_file1 = split_dir + 'chat' + suffix
#  read_file2 = split_dir + 'chat.dev' + suffix
  write_file = split_dir + 'vocab' + suffix
  create_vocab(rfile1=read_file1, wfile=write_file)
#  create_vocab(rfile1=read_file1, rfile2=read_file2, wfile=write_file)
