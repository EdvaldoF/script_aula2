#!/usr/bin/env python3

import pwd

#Lista dos usúarios do sistema

for user in pwd.getpwall():
    print(user.pw_name)
    