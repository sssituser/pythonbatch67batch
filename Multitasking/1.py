import threading
import time
class Game:
    def __init__(self,name):
        self.name = name
        
    def player(self):
        for i in range(1,11):
            print(f'Player {self.name} is Playing {i} time')
            time.sleep(3)      
sai = Game("nihar")
shiva = Game("nandu")
t1 = threading.Thread(target=sai.player,name='Thread-1') # unstarted state
t2 = threading.Thread(target=shiva.player,name='Thread-2')
t1.start()   # Ready state
t2.start()
t1.name = "first"
t2.name = "second"

# Pritorities of threads
                    
# Normal Abovenorml high
# belownormal lowest

# Thread Life Cycle Stages
# 1. Unstarted State : Creating object Threading class
# 2. Readay state : calling start method of a thread class
# 3. Running state of thread : Exucuting the Thread 
# 4. non runtable state : Thread is wating for some time
# 5. Dead state : Thread completes its execution of Aborting the thread is
# called is called Dead state.