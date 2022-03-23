# 2IN013 Groupe 3 - Projet Robotique 2021-2022
* Emails : (nicolas.baskiotis|olivier.schwander) [@] isir.upmc.fr
* Template Trello pour Scrum/Agile : https://trello.com/b/OjUJheXD/2i013-template


## Se connecter au robot 
* wifi : 2IN013-x (x=0..5) , password : GOPIGO2IN013
* Connection par ssh : ```ssh pi@192.168.13.1``` , password  : pi
* Transferer un repertoire local vers le robot : ```scp -r mon_repertoire pi@192.168.13.1:```
* Transferer un repertoire du robot vers local : ```scp -r pi@192.168.13.1:repetoire repertoire_dest```
* Monter un repertoire du robot sur sa machine : ```sshfs pi@192.168.13.1:repetoire repertoire_dest``` (ne pas oublier de faire un ```umount repertoire_dest``` à la fin)
* Executer un script sur le robot : ```python3 mon_script.py``` (**ne pas oublier python3 !!!**)
