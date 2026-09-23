import concurrent.futures

class ProcTaskRunner : 

    def __init__(self, n_workers = 10) : 
        self.n_workers = n_workers

    def run(self, task_func, args) : 
        n = 0
        n_tasks = len(args)
        results = []        
        
        with concurrent.futures.ProcessPoolExecutor(self.n_workers) as executor :             
            futures = [executor.submit(task_func, *arg) for arg in args] 

            for f in concurrent.futures.as_completed(futures) : 
                results.append( f.result() )

                n += 1
                print(f'{n / n_tasks:.2f} task done.')

        return results 
    
def test_task(n) : 
    return n**2
    
if __name__ == '__main__' : 
    task_runner = ProcTaskRunner()
    args = [ [n] for n in range(100000) ]
    results = task_runner.run(test_task, args)
    print(results)