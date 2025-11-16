*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  joku
    Set Password  jokujoku1
    Set Password Confirmation  jokujoku1
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jo
    Set Password  jokujoku1
    Set Password Confirmation  jokujoku1
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters long
    

Register With Valid Username And Too Short Password
    Set Username  joku
    Set Password  joku1
    Set Password Confirmation  joku1
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  joku
    Set Password  jokujoku
    Set Password Confirmation  jokujoku
    Click Button  Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  joku
    Set Password  jokujoku1
    Set Password Confirmation  jokujoku2
    Click Button  Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  jokujoku1
    Set Password Confirmation  jokujoku1
    Click Button  Register
    Register Should Fail With Message  Username is already taken

*** Keywords ***

Register Should Succeed
    Application Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page