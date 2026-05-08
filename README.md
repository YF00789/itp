# Advanced Calculator Project

## 1. Architectural Design & Block Diagram

The project uses a modular architecture, splitting the core mathematical logic away from data storage and the user interface. 

### Block Diagram

```text
                             +-------------------------+
                             |        main.py          |
                             | (CLI & Control Flow)    |
                             +-----------+-------------+
                                         |
                       +-----------------v-----------------+
                       |                                   |
            +----------v-----------+            +----------v-----------+
            |  calculator_logic/   |            |    data_storage/     |
            |    calculator.py     |            |      storage.py      |
            | (System Integration) |            |   (State Manager)    |
            +----------+-----------+            +----------+-----------+
                       |                                   |
        +--------------+---------------+                   |
        |                              |                   |
+-------v---------+            +-------v---------+   +-----v-----+
| calculator_logic|            | calculator_logic|   | Local OS  |
|  operations.py  |            |    utils.py     |   | .csv file |
| (Math/Core OOP) |            | (RegEx, Lambdas)|   | .json file|
+-----------------+            +-----------------+   +-----------+