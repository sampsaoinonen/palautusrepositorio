*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered
    
Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already used

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username too short. (Minimum 3 characters)

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  källe  kalle123
    Output Should Contain  Username must consist of characters from a to z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle12
    Output Should Contain  Password too short. (Minimum 8 characters)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password must not consist of letters only