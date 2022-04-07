  GNU nano 4.8                    You won the game                              
#!/bin/bash

echo "Enter any number"
read n

if [[ ( $n -eq 15 || $n -eq 45 ) ]]
then
echo "You won the game"
else
echo "You lost the game"
fi
