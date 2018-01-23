
import subprocess
import threading



class Miner:

    running = False

    miner = None
    
    def __init__(self):
        pass

    @property
    def params(self):
        return []

    @property
    def cmd(self):
        return [self.miner] + self.params

    def tear_down(self):
        pass

    def run(self):
        self.running = True
        p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while(True):
            # returns None while subprocess is running
            retcode = p.poll() 
            data = self.parse_output(p.stdout.readline())
            self.update(data)

        #     if not self.active:
        #         p.kill()
        #         print("Close signal sent")
        #         time.sleep(3)

        #     if(retcode is not None):
        #         print("Miner processed finished")
        #         break
        pass


class MinerDummy(Miner):

    miner = "./vendors/dummy/miner.sh"
    

    def parse_output(self):
        pass

    def update(self):
        pass



class Algorithm:
    
    def __init__(self, miner):
        self.__miner = miner


class AlgDummy(Algorithm):


    @property
    def params(self):
        return []




class Mining:
    

    def start():
        t = threading.Thread(target=worker, args=(i,))


if __name__ == "__main__":
    m = MinerDummy()
    m.run()

