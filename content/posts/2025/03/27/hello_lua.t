-- hello_lua.t
local C = terralib.includecstring [[
    #include <stdio.h>
    #include <stdlib.h>
]]

function say_hello(...)
    print("Hello, this is Lua!")
end

terra_say_hello = terralib.cast({}->{}, say_hello)

terra hello()
    terra_say_hello()
    return C.EXIT_SUCCESS
end

-- create the file "hello_lua" that we can run later
terralib.saveobj("hello_lua.o", {main=hello}, {"-avx"})
