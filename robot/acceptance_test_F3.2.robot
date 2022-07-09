| *** Settings ***    |
| Documentation       | This is test suite for acceptance test of functionality 3.2. Recognize
| Metadata            | Version | 1.0.0
| Metadata            | More Info | You can acces to the source code here: https://github.com/willyromero/acceptancetest-robotframework
| Metadata            | Executed At | ${HOST}
| Force Tags          | Functionality 3.2 Recognize
| Default Tags        | owner-willy_romero | 6668
| Resource            | Keywords.resource
| Library             | String 
| Library             | ../TestLibrary/RecognizeLibrary.py

| *** Variables ***        |
| &{DIC_PARAMETERS_TC1}    | probability=00 | name=willy
| &{DIC_PARAMETERS_TC2}    | probability=70 | name=willy
| &{DIC_PARAMETERS_TC3}    | probability=60 | name=willy
| &{DIC_PARAMETERS_TC4}    | probability=70 | name=willy
| &{DIC_PARAMETERS_TC5}    | probability=60 | name=willy

| ${RQ1 F 3 2}             | As an user I should known when camera was not started.
| ${RQ2 F 3 2}             | As an user I must see the message "Desconocido" when I wasn't recognized.
| ${RQ3 F 3 2}             | As an user I must see a message whit me name when I was recognized.
| ${RQ4 F 3 2}             | As an user I must see "Desconocido" message when I wasn't recognized and I should press key "escape".
| ${RQ5 F 3 2}             | As an user I must see a message whit me name when I was recognized and I should press key "escape".

| ${HOST}                  | Local.

| *** Test Cases ***       |
| No Camera Started        | [Documentation]       | ${RQ1 F 3 2}
|                          | Verify Test Case 1    | ${DIC_PARAMETERS_TC1}[probability] | ${DIC_PARAMETERS_TC1}[name]

| Unrecognized Face        | [Documentation]       | ${RQ2 F 3 2}
|                          | Verify Test Case 2    | ${DIC_PARAMETERS_TC2}[probability] | ${DIC_PARAMETERS_TC2}[name]

| Recognized Face          | [Documentation]       | ${RQ3 F 3 2}
|                          | Verify Test Case 3    | ${DIC_PARAMETERS_TC3}[probability] | ${DIC_PARAMETERS_TC3}[name]

| Unrecognized Face Key    | [Documentation]       | ${RQ4 F 3 2}
|                          | Verify Test Case 4    | ${DIC_PARAMETERS_TC4}[probability] | ${DIC_PARAMETERS_TC4}[name]

| Recognized Face Key      | [Documentation]       | ${RQ5 F 3 2}
|                          | Verify Test Case 5    | ${DIC_PARAMETERS_TC5}[probability] | ${DIC_PARAMETERS_TC5}[name]