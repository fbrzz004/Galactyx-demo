Project Development Secuence

    1. Secuence Analysis:
        Define the main sequence of actions that the player will follow within the game, based on the previosly established flow.

    2. Identification of Entities
        Identify the key entities in the game, sush as players, meteors, ships, etc. Define their characteristics and basic behaviors.

    3. Sprite Creation
        Create or find the necessary sprites for the entities identified in the previous step, ensuring that all visual elemtnss are available.

    4. State Machine Definition
        Establish the different game states (menu, options, levels view, game execution, settings, Game Over view) and how to transition between them.
        Note: This step can be done in parallel with sprite creation.

    5. General Sequence Implementation
        Create a general game secuence that integrates the menu, options, levels view, game execution, settings, and Game Over View. 
        This secuencie must align with the state machine defined in step 4.

    6. Game Executor Development
        Implement the <<gameExecutor>> class or interface, which will be responsible for executing the selected levels. this is the only interface
        that will be tied to the level you wnat to display.

    7. Level Design
        Develop the game levels and define businnes rules that prevent playing a level withhout completing the previous one, if necessary.

    8. Business Rules Verification
        Ensure that all identified business rules are respected, such as level progression, making sure the player cannot advance fulfilling prior requirements.

