
import arcade
import os

SPRITE_SCALING = 1
TOY_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Whack a Mole!"
RADIUS = 40

LOC1x = SCREEN_WIDTH / 1.35
LOC1y = SCREEN_HEIGHT / 1.35

LOC2x = SCREEN_WIDTH / 2
LOC2y = SCREEN_HEIGHT / 1.35

LOC3x = SCREEN_WIDTH / 4
LOC3y = SCREEN_HEIGHT / 1.35

LOC4x = SCREEN_WIDTH / 1.35
LOC4y = SCREEN_HEIGHT / 2

LOC5x = SCREEN_WIDTH / 2
LOC5y = SCREEN_HEIGHT / 2

LOC6x = SCREEN_WIDTH / 4
LOC6y = SCREEN_HEIGHT / 2

LOC7x = SCREEN_WIDTH / 1.35
LOC7y = SCREEN_HEIGHT / 4

LOC8x = SCREEN_WIDTH / 2
LOC8y = SCREEN_HEIGHT / 4

LOC9x = SCREEN_WIDTH / 4
LOC9y = SCREEN_HEIGHT / 4


MOVEMENT_SPEED = 5


class Player(arcade.Sprite):
    """ Player Class """

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

    def check_hit(self, score, total_time):
        if -40 < (self.center_y - LOC1y) < 40 and -40 < (self.center_x - LOC1x) < 40 and total_time % 1 == 1:
            score += 1
        elif -40 < (self.center_y - LOC2y) < 40 and -40 < (self.center_x - LOC2x) < 40 and total_time % 2 == 2:
            score += 1
        elif -40 < (self.center_y - LOC3y) < 40 and -40 < (self.center_x - LOC3x) < 40 and total_time % 3 == 3:
            score += 1
        elif -40 < (self.center_y - LOC4y) < 40 and -40 < (self.center_x - LOC4x) < 40 and total_time % 4 == 4:
            score += 1
        elif -40 < (self.center_y - LOC5y) < 40 and -40 < (self.center_x - LOC5x) < 40 and total_time % 5 == 5:
            score += 1
        elif -40 < (self.center_y - LOC6y) < 40 and -40 < (self.center_x - LOC6x) < 40 and total_time % 6 == 6:
            score += 1
        elif -40 < (self.center_y - LOC7y) < 40 and -40 < (self.center_x - LOC7x) < 40 and total_time % 7 == 7:
            score += 1
        elif -40 < (self.center_y - LOC8y) < 40 and -40 < (self.center_x - LOC8x) < 40 and total_time % 8 == 8:
            score += 1
        elif -40 < (self.center_y - LOC9y) < 40 and -40 < (self.center_x - LOC9x) < 40 and total_time % 9 == 9:
            score += 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        self.total_time = 0.0

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Background image will be stored in this variable
        self.background = None

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # --- Variables for our statistics

        # Time for on_update
        self.processing_time = 0

        # Time for on_draw
        self.draw_time = 0

        self.game_over = False

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)


    def setup(self):
        """ Set up the game and initialize the variables. """

        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

        self.total_time = 0.0

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = Player(":resources:images/animated_characters/male_person/malePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Figure out our output
        output = f"Time: {minutes:02d}:{seconds:02d}"

        # Output the timer text.
        arcade.draw_text(output, 300, 550, arcade.color.BLACK, 30)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 550, arcade.color.BLACK, 18)


        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 1.35, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLACK
        )

        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, RADIUS, arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4, RADIUS, arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 1.35, SCREEN_HEIGHT / 4, RADIUS, arcade.color.BLACK
        )

        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.35, RADIUS, arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 4, SCREEN_HEIGHT / 1.35, RADIUS, arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 1.35, SCREEN_HEIGHT / 1.35, RADIUS, arcade.color.BLACK
        )

        # Draw all the sprites.
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()

        self.total_time += delta_time




    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.W or key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            self.player_sprite.check_hit(self, self.score, self.total_time)


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.W or key == arcade.key.S or key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D or key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
