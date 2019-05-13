box.cfg {
    listen = '3301'
}

box.once('v1', function()
    local s = box.schema.space.create('place')
    s:format({
        { name = 'code', type = 'string' },
        { name = 'name', type = 'string' },
    })
    s:create_index('primary', {type = 'hash',parts = {'code'}})
end)

box.once('v1', function()
    box.schema.user.grant('guest', 'read,write,execute', 'universe')

    box.sql.execute([[
        create table users (
            id int primary key,
            name text
        )
    ]])
end)

box.once('v1', function()
    box.schema.user.grant('guest', 'read,write,execute', 'universe')
end)

queue = require('queue')
queue.create_tube('test_tube', 'fifottl')