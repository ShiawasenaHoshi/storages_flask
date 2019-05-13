box.cfg {}

box.once('v1', function()
    local s = box.schema.space.create('place')
    s:format({
        { name = 'code', type = 'string' },
        { name = 'name', type = 'string' },
    })
    s:create_index('primary', { type = 'hash', parts = { 'code' } })

    local t = box.schema.space.create('tester')
    t:format({
        { name = 'id', type = 'unsigned' },
        { name = 'name', type = 'string' },
    })
    t:create_index('primary')

    local u = box.schema.space.create('users')
    u:format({
        { name = 'id', type = 'unsigned' },
        { name = 'name', type = 'string' },
    })
    u:create_index('primary')
end)

queue = require('queue')
queue.create_tube('test_tube', 'fifottl')