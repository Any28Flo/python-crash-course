# Verify user

status : 

last update: 15- jun- 2023

author : Daedra

<hr/>

The final listing for _remember_me.py_ assumes either that the user has already entered their
username or that the program is running for the first time. We should modifiy it in case
the current user is not the person who last used the program.
Before printing a welcome back message in _greet_user()_, ask the user if this is the correct 
username. If it's not, call _get_new_username()_ to get the correct username.

```python
 user={
    "last_login" 
    "loggin_attemps"
}
```

