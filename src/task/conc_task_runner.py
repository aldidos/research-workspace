import concurrent.futures

class ConcurTaskRunner : 

    def __init__(self, n_workers = 12) : 
        self.n_workers = n_workers

    def run(self, task_func, args) : 
        n = 0
        results = []        
        
        with concurrent.futures.ThreadPoolExecutor(self.n_workers) as executor : 
            futures = [executor.submit(task_func, *arg) for arg in args] 

            for f in concurrent.futures.as_completed(futures) :
                results.append( f.result() )

                n += 1
                print(f'{n} task done.')

        return results 
    
def test_task(n) : 
    return n**2
    
if __name__ == '__main__' : 
    task_runner = ConcurTaskRunner(128)
    args = [ [n] for n in range(100000) ]
    results = task_runner.run(test_task, args)
    print(results)