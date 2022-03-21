# Python OOP for text adventure game
This is an outline for a simple text based adventure game using Python Object Oriented Programming
## Design:
* Each stage of the story is an object with these attributes:
  *  Text: the body of the story
  *  Options for player to choose. This include 2 sub attributes: the text to describe the option and the name of child stage that this option lead to.
* All of the game content will be stored in a json file
* Objects are stored as a dictionary in the json file
* The stages tree will be tracked by a flowchart
