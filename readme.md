# Fun With Flags

Simple AI network based to predict a low-res drawing of a flag.

Eventually this will become a game where you're told to draw a flag and just have to make it good enough for the AI to predict it.

## Design

Flags come in as a 3d array. 6x10x7 (width x height x number of colours). Every pixel is going to be either a 1 or a 0.

We can then flatten out the flag and stick it into a dense neural network. Originally I was thinking of doing a convolutional ntwork, but I'm not sure how well that'd work with the colours? I think we'd then have to try and compress the colours into a single integer. Best way I can think of doign that is basically just using saturation, but I don't think it'll be great at predicting from greyscale.

Network will take an input [420] which will push trough to 2 further [420] layers and finally ending on a [49] layer. This then pushes into a softmax to generate probabilities. We then take the highest probability and predict the flag.

## The Game

The idea of the game is to present the name of a country and make the user draw the flag of the country (obviously in their extemely small grid). The AI will preduict the flag. Your score goes up by 2 if your flag is the first guess, 1 if it's the second or third gures, and if your flag isn't predicted then it's game over.

I intended to maybe try and make this using a Python UI (like with PyQt), but I think I'm instead going to try and make this in HTML / CSS / JS. Either I can pass the flag into a DB, or I can try and code the network into JS with the hard-coded weights. 
