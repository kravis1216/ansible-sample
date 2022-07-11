import logging
import sys
import time #タイムスタンプ情報を保持

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

class BlockChain(object):
  def __init__(self):
      # トランザクション情報を格納するプール
      self.transaction_pool = []
      self.chain = []
      self.create_block(0, 'init hash')

  def create_block(self, nonce, previous_hash):
      block = {
          'timestamp': time.time(),
          'transactions': self.transaction_pool,
          'nonce': nonce,
          'previous_hash': previous_hash
      }
      self.chain.append(block)
      self.transaction_pool = []
      return block

# 見やすくする関数
def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} Chain {i} {"="*25}')
        for k,v in chain.items():
            print(f'{k:15}{v}')
    print(f'{"*"*25}')

# スクリプトが直接実行された時に実行される処理
if __name__ == '__main__':
    block_chain = BlockChain()
    pprint(block_chain.chain)
    block_chain.create_block(3, 'hash 2')
    pprint(block_chain.chain)