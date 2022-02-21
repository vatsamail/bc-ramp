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
        print("Mining condition: The hash should contain both 'F' and 'U'. Content:", self.content)


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
        

class DecentBlockChain():
    def __init__(self):
        self.bc1 = BlockChain()
        self.bc2 = BlockChain()
        self.bc3 = BlockChain()

   
    def add(self, block):
        self.bc1.add(block)
        self.bc2.add(block)
        self.bc3.add(block)

    
    def show(self):
        if len(self.bc1.chain) == len(self.bc2.chain):
            if len(self.bc3.chain) == len(self.bc1.chain):
                print("Chain Length is the same:", len(self.bc1.chain))
            else:
                print("Chain Length of bc3 is corrupted! bc1 and bc2:", len(self.bc1.chain), "but bc3:", len(self.bc3.chain))
        else:
            if len(self.bc3.chain) == len(self.bc1.chain):
                print("Chain Length of bc2 is corrupted! bc1 and bc3:", len(self.bc1.chain), "but bc2:", len(self.bc2.chain))
            else:
                if len(self.bc3.chain) == len(self.bc2.chain):
                    print("Chain Length of bc2 is corrupted! bc2 and bc3:", len(self.bc2.chain), "but bc1:", len(self.bc1.chain))
                else:
                    print("All chain lengths are different!", "bc1:", len(self.bc1.chain), "bc2:", len(self.bc2.chain), "bc3:", len(self.bc3.chain))

        
        for i, b in enumerate(self.bc1.chain):
            if (self.bc1.chain[i].content == self.bc2.chain[i].content):
                if (self.bc2.chain[i].content == self.bc3.chain[i].content):
                    print("\nBlock Index:", i, "\nBlock Hash:", self.bc1.chain[i].hash, \
                        "\nPrevious Hash:", self.bc1.chain[i].prev, \
                            "\nBlock Number:", self.bc1.chain[i].block, \
                                "\nBlock Nounce:", self.bc1.chain[i].nounce, \
                                    "\nBlock Content:", self.bc1.chain[i].content)
                else:
                    print("BC3 is corrupt. Fixing it.")
                    self.bc3 = self.bc1.copy()
                
            else:
                if (self.bc2.chain[i].content == self.bc3.chain[i].content):
                    print("BC1 is corrupt. Fixing it.")
                    self.bc1 = self.bc2.copy()

                else:
                    if (self.bc1.chain[i].content == self.bc3.chain[i].content):
                        print("BC2 is corrupt. Fixing it.")
                        self.bc2 = self.bc1.copy()
                    else:
                        print("Everything is corrupt.")
                        exit()
        
                   



def main():
    bc = DecentBlockChain()
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

    b3.content = "hacking"
    bc.show()
    



    

if __name__ == '__main__':
    main()
