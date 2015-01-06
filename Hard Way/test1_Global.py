def bob():
    global me
    me = "locally defined"   # Defined locally but declared as global
    print me

bob()
print me     # Asking for a global variable
