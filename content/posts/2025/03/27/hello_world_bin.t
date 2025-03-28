-- hello_world_bin.t
local C = terralib.includecstring [[
    #include <stdio.h>
    #include <stdlib.h>
]]

-- hello will be our main function, check bellow when we save this program
terra hello()
    C.printf("Hello, Terra!\n")
    return C.EXIT_SUCCESS
end

-- create the file "helloterra" that we can run later
terralib.saveobj("helloterra", {main=hello})