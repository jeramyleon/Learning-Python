print("""
------------------------------------------------------------------------
DATABASE NORMALIZATION (3NF)
- There is "tons" of database theory - way too much to understand without 
excessive predicate calculus 
- Do not replicate data - reference data - point at data 
- Use integers for keys and for references 
- Add a special "key" column to each table which we will make references to.
By convention, many programmers call this column "id" 
------------------------------------------------------------------------
INTEGER REFERENCE PATTERN 
- We use integers to reference rows in another table 
-------------------------------------------------------------------------
THREE KINDS OF KEYS 
- Primary key - generally an integer auto-increment field
- Logical key - What the outside world uses for lookup 
- Foreign key - generally an integer key pointing to a row in another 
table 
------------------------------------------------------------------------
KEY RULES 
Best practices 
    - Never use your logical key as the primary key 
    - Logical keys can and do change, albeit slowly
    - Relationships that are based on matching string fields are less 
    efficient than integers 
-----------------------------------------------------------------------
FOREIGN KEYS
- A foreign key is when a table has a column that contains a key which 
points to the primary key of another table 
- When all primary keys are integers, then all foreign keys are integers - 
this is good - very good
---------------------------------------------------------------------

""")