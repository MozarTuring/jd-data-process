from emb_vocab import load_embed_txt, load_vocab

suffix = '.dec'
split_dir = 'jieba_split/'
emb_file = split_dir + 'emb_word' + suffix
voc_file = split_dir + 'vocab' + suffix
write_file = split_dir + 'vocab_re' + suffix

emb_dict, _ = load_embed_txt(emb_file)
_, _, vocab = load_vocab(voc_file)

trainable_tokens = []
const_tokens = []

for vo in vocab:
  if vo in emb_dict:
    const_tokens.append(vo)
  else:
    trainable_tokens.append(vo)

with open(write_file, 'w', encoding='utf-8') as f:
  for tra in trainable_tokens:
    f.write(tra + '\n')

  for con in const_tokens:
    f.write(con + '\n')

