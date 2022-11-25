# Hangman

## Description

Let's play a game. We are not going to start hanging people literally, but if the player doesn't find the hidden word he will hang the stickman.

The objective of the game is simple, the computer will hide a random word and the player will have to find out what the word is by saying letters, for each letter he misses, the stickman will become more visible.

## Example

```text
_ _ _ _ 

________ 
|      | 
|        
|        
|        
|        
```
```text
Input - a
````

```text
_ _ _ _ 
a 
________ 
|      | 
|      O 
|        
|        
|        
```
```text
Input - e
````


```text
_ _ _ _ 
a e 
________ 
|      | 
|      O 
|     /  
|        
|        
```
```text
Input - o
````

```text
_ o o _ 
a e o 
________ 
|      | 
|      O 
|     /  
|        
|        
```
```text
Input - o
````

etc....

```text
_ o o _ 
a e o q w r t 
________ 
|      | 
|      O 
|     /|\
|     / \
|        
```
