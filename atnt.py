#from https://github.com/igorcoding/asynctnt and https://github.com/tarantool/queue-python
import asynctnt
import asynctnt_queue


async def basic_usage():
    conn = asynctnt.Connection(host='127.0.0.1', port=3301)
    await conn.connect()

    for i in range(1, 11):
        await conn.insert('tester', [i, 'hello{}'.format(i)])

    data = await conn.select('tester', [])
    first_tuple = data[0]
    print('tuple:', first_tuple)
    print(f'tuple[0]: {first_tuple[0]}; tuple["id"]: {first_tuple["id"]}')
    print(f'tuple[1]: {first_tuple[1]}; tuple["name"]: {first_tuple["name"]}')

    for i in range(1, 11):
        await conn.delete('tester', [i])

    await conn.disconnect()


# todo not working
async def sql_usage():
    conn = asynctnt.Connection(host='127.0.0.1', port=3301)
    await conn.connect()

    await conn.sql("insert into users (id, name) values (1, 'James Bond')")
    await conn.sql("insert into users (id, name) values (2, 'Ethan Hunt')")
    data = await conn.sql('select * from users')

    for row in data:
        print(row)

    await conn.disconnect()


async def queue_usage():
    conn = asynctnt.Connection(host='127.0.0.1', port=3301)
    await conn.connect()

    queue = asynctnt_queue.Queue(conn)
    test_tube = queue.tube('test_tube')

    # Add a task to queue
    task = await test_tube.put({
        'key': 'value'
    })

    print('Task id: {}'.format(task.task_id))
    print('Task status: {}'.format(task.status))

    # Retrieve a task from queue
    task = await test_tube.take(1)

    # ... do some work with task

    await task.ack()
    await conn.disconnect()
