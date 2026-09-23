import asyncio

class AsyncTaskRunner : 

    async def run(task_func, args) : 
        temp_results = []

        async with asyncio.TaskGroup() as tg : 
            temp_results.extend( [ tg.create_task( task_func(*arg) ) for arg in args ] ) 

        results = [ task.result() for task in temp_results ]        
        return results

async def test_func(x) : 
    return x**2

async def main() : 
    args = [ [n] for n in range(100000) ]
    results = await AsyncTaskRunner.run(test_func, args)
    print(results)
    
if __name__ == '__main__' : 
    asyncio.run(main())    