# Simple Ordering System ( Compro-1 Final exam )

This is my final exam in the course Computer Programming-I about design and implementing OOP files from scratches.
## File Structure

- `oop.py`: Defines the `Person` `Customers` `Driver` `DeliveryOrder` classes with attributes and methods that coposited and inherited.
- `Readme.md`: This file providing details and instructions.

## Classes

### Person
- Parent class that has childs :
  - Customer
  - Driver
    
### Customer
- Using attributes _"name"_ from `Person` class
- Has method to place order `items` for DeliveryOrder and create DeliveryOrder object
  
### Driver 
- Using attributes _"name"_ from `Person` class
- Has method to update status

### DeliverOrder
- Composited to **Customer** and **Driver**
- Has method to assgin driver object ( driver.name )
- Includes all data : _Customer_ , _Item_ , _Status_

## Sample Output
<img width="524" height="534" alt="final" src="https://github.com/user-attachments/assets/a046577a-8422-4001-be62-9bc0abbd5998" />


Including: 
- 3 persons
- 2 orders

##  Running the file

To run the order system, execute `oop.py`:

```bash
python oop.py
