# tic-tac-toe
A tic-tac-toe game architected as a Web Service API using Google App Engine.

## Link to app
  [Tic-Tac-Toe](game-911.appspot.com)

## Set-Up Instructions:
1.  Update the value of application in app.yaml to the app ID you have registered
 in the App Engine admin console and would like to use to host your instance of this sample.
1.  Run the app with the devserver using dev_appserver.py DIR, and ensure it's
 running by visiting the API Explorer - by default localhost:8080/_ah/api/explorer.
1.  (Optional) Generate your client library(ies) with the endpoints tool.
 Deploy your application.

2. Instructions to play the game:
   - Create 2 users with Create User Button
   - Create A New Game with the 2 users previously created (User1 will be PLAYER_X, User 2 will be PLAYER_O), Show Game button will appear
   - Click Show Game and make some moves
   - While playing the game, you can click Show History in order to show all the moves that have been made
   - You can cancel a game by clicking Cancel Game button
   - You can see a User games by clicking Get User Games
   - You can see all Users rankings by clicking Get User Rankings


##Game Description:
Tic Tac Toe is a simple 2-player game. There is a 3x3 table. First player selects
where to put X, second player selects where to put O. The first player with 3 same
values in a row or in a column or in diagonal wins.
The players need to be registered first.
Many different Tic Tac Toe games can be played by many different Users at any
given time. Each game can be retrieved or played by using the path parameter
`urlsafe_game_key`.

###A table looks like this:
|  0  |  1  |  2  |
|-----|-----|-----|
|  3  |  4  |  5  |
|  7  |  8  |  9  |

0,1,2,3,4,5,6,7,8 are the positions that is send to the API when a user makes a move. This number is also
reflected in the game history.
When a game ends and it isn't a draw, the user that wins receives 1 point, the user that looses receives -1 point.

##Files Included:
 - static/css/main.css: Frontend styling.
 - static/js/vendor/angular-local-storage.min.js: External library for storing data into localStorage with Angular.
 - static/js/app.js: Defines game main module and available routes.
 - static/js/controllers.js: Defines game controllers for frotend part.
 - static/partials/create-user.html: Create user modal layout.
 - static/partials/home.html: Main content layout.
 - static/partials/new-game.html: New game modal layout.
 - static/partials/user-games.html: User games modal layout.
 - templates/index.html: Starting point of frontend app.
 - api.py: Contains endpoints and game playing logic.
 - app.yaml: App configuration.
 - cron.yaml: Cronjob configuration.
 - main.py: Handler for cronjob.
 - models.py: Entity and message definitions including helper methods.
 - utils.py: Helper function for retrieving ndb.Models by urlsafe Key string.

##Endpoints Included:
 - **create_user**
    - Path: 'user'
    - Method: POST
    - Parameters: user_name (required), email (optional)
    - Returns: Message confirming creation of the User.
    - Description: Creates a new User. user_name provided must be unique. Will
    raise a ConflictException if a User with that user_name already exists.

 - **new_game**
    - Path: 'game'
    - Method: POST
    - Parameters: user_name1, user_name2
    - Returns: GameForm with initial game state.
    - Description: Creates a new Game. user_name1, user_name2 provided must correspond to
    existing users - will raise a NotFoundException if not.

 - **get_game**
    - Path: 'game/{urlsafe_game_key}'
    - Method: GET
    - Parameters: urlsafe_game_key
    - Returns: GameForm with current game state.
    - Description: Returns the current state of a game.

 - **get_user_games**
    - Path: 'game/user/{user_name}'
    - Method: GET
    - Parameters: user_name
    - Returns: GameForms with all the active games the user is playing.
    - Description: Returns all the active games the user is playing.

 - **get_user_rankings**
    - Path: 'user/ranking'
    - Method: GET
    - Parameters: None
    - Returns: UserRankingsForm with all users and how many wins and losses they have.
    - Description: Returns all users and how many wins and losses they have.

 - **cancel_game**
    - Path: 'game/cancel/{urlsafe_game_key}'
    - Method: PUT
    - Parameters: urlsafe_game_key
    - Returns: GameForm with cancelled property True.
    - Description: Returns game with cancelled property True.

 - **make_move**
    - Path: 'game/{urlsafe_game_key}'
    - Method: PUT
    - Parameters: urlsafe_game_key, position
    - Returns: GameForm with new game state.
    - Description: Accepts a 'position' and returns the updated state of the game.
    If this causes a game to end, a corresponding Score entity will be created.

 - **get_game_history**
    - Path: 'game/history/{urlsafe_game_key}'
    - Method: GET
    - Parameters: urlsafe_game_key
    - Returns: GameHistoryForms with all the moves that have been played for the current game.
    - Description: Gets the history of moves for current game stored in memcache.


##Models Included:
 - **User**
    - Stores unique user_name, email address and score. If the user won a game receives 1 point, if
    he lost receives -1 point, if it was a draw he doesn't receive any point.

 - **GameHistory**
    - Stores game history for one game.

 - **Game**
    - Stores unique game states. Associated with User model via KeyProperty.


##Forms Included:
 - **GameForm**
    - Representation of a Game's state (urlsafe_key, message, user_name1, user_name2,
    current_player, board, cancelled flag, game_over flag, email_reminder_sent flag). A board is a list of Strings initialized
    with 9 empty strings, and as a player makes a move, the position is filled with PLAYER_X or
     PLAYER_O value.
 - **GameForms**
    - Multiple FameForm container.
 - **NewGameForm**
    - Used to create a new game (user_name1, user_name2)
 - **MakeMoveForm**
    - Inbound make move form (position).
 - **UserRankingForm**
    - Representation of a user ranking (user_name, score).
 - **UserRankingsForm**
    - Multiple UserRankingForm container.
 - **GameHistoryForm**
    - Representation of a game history(username, position, message).
 - **GameHistoryForms**
    - Multiple GameHistoryForm container.
 - **StringMessage**
    - General purpose String container.

##References:
 1. [https://developers.google.com/appengine](https://developers.google.com/appengine)
 2. [https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool](https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool)
 3. [https://developer.apple.com/library/safari/samplecode/TicTacToe/Introduction/Intro.html](https://developer.apple.com/library/safari/samplecode/TicTacToe/Introduction/Intro.html)

