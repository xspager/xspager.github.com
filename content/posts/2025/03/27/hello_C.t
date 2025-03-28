-- hello_C.t
-- assing symbols in stdio.h to the variable C
C = terralib.includec("stdio.h")

-- this is how you call a C function
C.printf("Hello, C!\n")
