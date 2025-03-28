-- hello_world_args.t
-- A variation on the classic Hello, World that prints the parameters
local C = terralib.includecstring [[
    #include <stdio.h>
    #include <stdlib.h>
]]

-- hello will be our main function so we accept argc and argv
terra hello(argc : int, argv : &rawstring)
    -- this is how you call a C function
    C.printf("Hello, Terra!\n")
    if argc > 1 then
        var i = 0
        while i < argc do
            C.printf("argv[%i] %s\n", i, argv[i])
            i = i + 1
        end
    end
    return C.EXIT_SUCCESS
end

terralib.saveobj("helloargs", {main=hello})