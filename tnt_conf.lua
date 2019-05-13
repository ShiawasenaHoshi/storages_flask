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
