import random

RATIO_TRAIN = 0.7

def train_dev_split(split_dir):
  readfi1 = split_dir + 'chat.enc'
  readfi2 = split_dir + 'chat.dec'
  writefi1 = split_dir + 'chat.train.enc'
  writefi2 = split_dir + 'chat.train.dec'
  writefi3 = split_dir + 'chat.dev.enc'
  writefi4 = split_dir + 'chat.dev.dec'
  with open(readfi1, 'r', encoding='utf8') as rf1:
      with open(readfi2, 'r', encoding='utf8') as rf2:
          with open(writefi1, 'w', encoding='utf8') as wf1:
              with open(writefi2, 'w', encoding='utf8') as wf2:
                  with open(writefi3, 'w', encoding='utf8') as wf3:
                      with open(writefi4, 'w', encoding='utf8') as wf4:
                          lines1 = rf1.readlines()
                          lines2 = rf2.readlines()
                          l_lines = len(lines1)
                          assert len(lines1) == len(lines2)
                          l_train = int(l_lines * RATIO_TRAIN)

                          train_samples = random.sample(range(l_lines), l_train)
                          dev_samples = set(range(l_lines)) - set(train_samples)
                          # train enc
                          for ind in train_samples:
                              wf1.write(lines1[ind])
                          # train dec
                          for ind in train_samples:
                              wf2.write(lines2[ind])
                          # dev enc
                          for ind in dev_samples:
                              wf3.write(lines1[ind])
                          # dev dec
                          for ind in dev_samples:
                              wf4.write(lines2[ind])

if __name__ == '__main__':
  train_dev_split('jieba_split/')
