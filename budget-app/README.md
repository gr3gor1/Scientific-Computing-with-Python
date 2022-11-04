The point of this project is to complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

  A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the     ledger list in the form of {"amount": amount, "description": description}.

  A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds,     nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.

  A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
  
  A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer     to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source         Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False       otherwise.
  
  A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True           otherwise. This method should be used by both the withdraw method and transfer method.

An example of the expected output is given below :

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

In order to complete the project there has to be a function that creates a chart such as the on given below :

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

The point of this chart is to describe the percentage of money per category.


Check the full description of the project here : https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

Chech the functional project on replit : https://replit.com/join/jrvvotxsbj-grigoriospapani
