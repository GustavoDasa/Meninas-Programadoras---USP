'''
INTRODUCTION

This version of the game supports many players. It is played with two full decks (52 cards each) and one joker (mico in this game), so each card except the wild card has a pair. Cards are dealt to all players: the number of cards for each player varies according to the number of players and not all players have the same number of cards in their hand. A player's objective is to get rid of all his cards. For this a player, being in possession of a pair of identical cards, gets rid of the pair by placing it on the table. Whoever gets rid of all the cards first wins.

ASSIGNMENT

Your program must read a player's cards and verify that they have the joker.

Input

Two lines. The first one contains the player's name. The second contains the list of cards in the player's possession.
'''

nome = input('Insira o nome: ')
cartas = input('\nInsira as cartas: ').split(' ')

if 'mico' in cartas:
  print(nome,'mico!')
else:
  print(nome,'ok')