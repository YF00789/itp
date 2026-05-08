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

---

## 2. Data Definitions

### A. Data Types Utilized
- `float`: Used for mathematical inputs (num1, num2) and outputs (result) to support decimals.
- `int`: Used for generating unique operation IDs (random.randint).
- `str`: Used for user input, operator symbols (+, -), file names, and regex patterns.
- `tuple`: Returned by validate_expression() to pass immutable, ordered parsed data (float, str, float).
- `list`: Used to hold the __history of operations and data retrieved from JSON.
- `dict`: Used for mapping operators to classes (self.operations) and formatting individual log entries.
- `set`: Used (self.unique_operators) to maintain an un-duplicated collection of operator types used in the session.
- `generator`: Yielded by history_generator for lazy-evaluation of the history list.

### B. Key System Variables
- `choice` (str): Stores the user's main menu selection.
- `expr` (str): The raw string math expression inputted by the user (e.g., "5 * 3").
- `num1`, `num2` (float): The operands unpacked from the user's expression.
- `op` (str): The mathematical operator (+, -, *, /, ^).
- `self.json_file`, `self.csv_file` (str): Encapsulated file paths in StorageManager.
- `self.unique_operators` (set): Tracks the distinct mathematical operations performed.
- `self.__history` (list of dict): Private, encapsulated list storing the session's calculation state.
- `self.operations` (dict): The mapping dictionary connecting a string operator ("+") to an instantiated OOP class (Add()).

### C. File Types
- `.py`: Core Python script and module files.
- `.json`: Used for structured, persistent data storage of calculation history.
- `.csv`: Used for flat, table-like data exports of the history log.
- `.md`: Markdown file for documentation.
- `.txt`: Text file used to outline project dependencies (requirements.txt).

### D. OOP Components
- Classes: 
  - StorageManager: Handles OS/File I/O and state persistence.
  - Operation (Abstract Base Class / ABC): Defines the contract for all math operations.
  - Add, Subtract, Multiply, Divide, Power: Concrete implementations of Operation.
  - Calculator: The main engine linking storage and mathematical operations.
- Inheritance: Add, Subtract, etc., inherit from the Operation base class.
- Polymorphism: The execute(a, b) method is implemented differently in each child class. The Calculator routes input to .execute() dynamically without needing to know *which* class it is currently calling.
- Encapsulation: The calculator history is hidden within self.__history to prevent external modification, accessed only safely via get_history().
- Association: Calculator has-a StorageManager.