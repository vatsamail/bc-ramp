import hashlib, base64


class BlockChain():
    def __init__(self, block=None):
        self.chain = []
        if block:
            self.add(block)

    def add(self, block):
        self.chain.append(block)


class Block():
    def __init__(self, content):
        self.block = 1
        self.content = content
        self.nounce = 0
        self.prev = 0
        self.mine(self.block, self.content, self.prev)


    def mine(self, block, content, prev):
        hash = ''
        nounce = 0
        for i in range(9999999):
            (worked, hash) = self._condition(self.block, self.content, self.prev, i)
            if worked:
                break
        
        self.hash = hash
        self.nounce = i

        
    
    def _condition(self, block, content, prev, i):
        concat_string = str(block)+str(content)+str(prev)+str(i)
        concat_string = concat_string.encode()
        bit_str = hashlib.md5((concat_string)).digest()
        bit_str = base64.b64encode(bit_str)
        bit_str = bit_str.decode('utf-8')

        # solve to ensure 'X' is always in the hash string
        if 'F' in bit_str and 'U' in bit_str:
            return (True, bit_str)
        return (False, bit_str)

    def show(self):
        print("Block Number:", self.block,  "| Derived Nounce:", self.nounce, "| Previous Hash:", self.prev, "| This Hash:", self.hash, "| Content:", self.content)

    def update(self, block, prev):
        self.block = block
        self.prev = prev
        self.mine(self.block, self.content, self.prev)

    def addBlock(self, content):
        nb = Block(content)
        nb.update((self.block + 1), self.hash)
        return nb
        

    

def main():
    bc = BlockChain()
    seed = Block("vatsa")
    bc.add(seed)

    b2 = seed.addBlock("prahallada")
    bc.add(b2)

    b3 = b2.addBlock("vatsa")
    bc.add(b3)

    b4 = b3.addBlock("Awesome")
    bc.add(b4)

    b5 = b4.addBlock("Lets' end this!")
    bc.add(b5)
    

    for b in bc.chain:
        b.show()





if __name__ == '__main__':
    main()
