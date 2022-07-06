## Music Player
*With this App You Can See a list of your Songs and you can play/pause/unpause/stop them!*

![Music Player](/music_player.png)

### Needed Packages:
``` python
pip install pygame
pip install tk
```
### Pygame Mixer Example:
``` python
import pygame
mixer.init()
mixer.music.load("music path")
mixer.music.play() # plays the selected music
mixer.music.pause() # pauses the selected music
mixer.music.unpause() # un-pauses the selected music
mixer.music.stop() # stops the selected music
```