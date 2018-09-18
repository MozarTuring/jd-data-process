import codecs
import tensorflow as tf

def load_embed_txt(embed_file):
  emb_dict = dict()
  emb_size = None
  with codecs.getreader('utf-8')(tf.gfile.GFile(embed_file, 'rb')) as f:
    for line in f:
      tokens = line.strip().split(" ")
      word = tokens[0]
      vec = list(map(float, tokens[1:]))
      emb_dict[word] = vec
      if emb_size:
        assert emb_size == len(vec), "all embedding size should be the same"
      else:
        emb_size = len(vec)

  return emb_dict, emb_size


def load_vocab(vocab_file):
  vocab = []
  values = []
  with codecs.getreader('utf-8')(tf.gfile.GFile(vocab_file, 'rb')) as f:
    vocab_size = 0
    for word in f:
      vocab_size += 1
      word_ = word.strip()
      if word_ != '':
        vocab.append(word_)
        values.append(len(vocab))

  return dict(zip(vocab, values)), vocab_size, vocab

if __name__ == '__main__':
  suffix = '.dec'
  emb_file = '/home/team447/notespace/data/emb_word' + suffix
  split_dir = 'jieba_split/'
  voc_file = split_dir + 'vocab' + suffix
  write_file = split_dir + 'emb_word' + suffix
  
  vocab, vocab_size, _ = load_vocab(voc_file)
  print('vacab size is %d' % (vocab_size))
  print('lenth of vocab is %d' % (len(vocab)))

  with open(write_file, 'w', encoding='utf8') as wf:
    with open(emb_file, 'r', encoding='utf8') as rf:
      t = 0
      for line in rf:
        t += 1
        if t % 1000 == 0:
          print(t)
        tokens = line.strip().split(" ")
        word = tokens[0]
        if word in vocab:
          wf.write(line)

