
| *** Keywords ***      |
| Verify Test Case 1    | [Documentation]                | Camera of device was not started.
|                       | [Arguments]                    | ${probability} | ${name}
|                       | Camera No Started              | ${probability} | ${name}
|                       | Check Camera No Started        | cp1

| Verify Test Case 2    | [Documentation]                | The person scanned was unrecognized.
|                       | [Arguments]                    | ${probability} | ${name}
|                       | Unrecognized Face              | ${probability} | ${name}
|                       | Check Unrecognized Face        | cp2

| Verify Test Case 3    | [Documentation]                | The person scanned was recognized.
|                       | [Arguments]                    | ${probability} | ${name}
|                       | Recognized Face                | ${probability} | ${name}
|                       | Check Recognized Face          | cp3

| Verify Test Case 4    | [Documentation]                | The person scanned was unrecognized and press key scape.
|                       | [Arguments]                    | ${probability} | ${name}
|                       | Unrecognized Face Key          | ${probability} | ${name}
|                       | Check Unrecognized Face Key    | cp4

| Verify Test Case 5    | [Documentation]                | The person scanned was recognized and press key scape.
|                       | [Arguments]                    | ${probability} | ${name}
|                       | Recognized Face Key            | ${probability} | ${name}
|                       | Check Recognized Face Key      | cp5