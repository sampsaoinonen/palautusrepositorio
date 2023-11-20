*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
 

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kaltsu
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials 
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Page Should Contain  Username too short. (Minimum 3 characters)

Register With Valid Username And Invalid Password
    Set Username  jore
    Set Password  jore
    Set Password Confirmation  jore
    Submit Credentials
    Page Should Contain  Password invalid. (Min. 8 characters and must also include other characters than letters)

Register With Nonmatching Password And Password Confirmation
    Set Username  pertti    
    Set Password  pertti123
    Set Password Confirmation  kalle123
    Submit Credentials 
    Page Should Contain  Password and Password confirmation are different

Login After Successful Registration
    Set Username  simo    
    Set Password  simo1234
    Set Password Confirmation  simo1234
    Submit Credentials
    Registration Should Succeed
    Go To Login Page
    Set Username  simo    
    Set Password  simo1234
    Submit login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  jepu    
    Set Password  jepu
    Set Password Confirmation  jepu
    Submit Credentials
    Registration Should Fail
    Go To Login Page
    Set Username  jepu  
    Set Password  jepu
    Submit login Credentials
    Login Should Fail
    
*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit login Credentials
    Click Button  Login


Login Should Succeed
    Main Page Should Be Open

Registration Should Succeed
    Title Should Be  Welcome to Ohtu Application! 

Registration Should Fail
    Register Page Should Be Open

Login Should Fail
    Login Page Should Be Open