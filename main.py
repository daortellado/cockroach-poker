from aiohttp import web
import socketio
import random

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)

# we can define aiohttp endpoints just as we normally
# would with no change
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for

@sio.on('playerCount')
async def print_message(sid, playerCount):
    print("Socket ID: " , sid)
    print(playerCount)
    cards = ['Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider', 'Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider', 'Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider', 'Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider', 'Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider', 'Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider', 'Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider', 'Bat', 'Fly', 'Cockroach', 'Toad', 'Rat', 'Scorpion', 'Stink Bug', 'Spider']
    random.shuffle(cards)
    hand1 = []
    hand2 = []
    hand3 = []
    hand4 = []
    hand5 = []
    hand6 = []
    if playerCount == 2:
        hand1 = cards[0:32]
        hand2 = cards[32:64]
        await sio.emit('hand1', hand1)
        await sio.emit('hand2', hand2)
    elif playerCount == 3:
        hand1 = cards[0:21]
        hand2 = cards[21:42]
        hand3 = cards[42:64]
        await sio.emit('hand1', hand1)
        await sio.emit('hand2', hand2)
        await sio.emit('hand3', hand3)
    elif playerCount == 4:
        hand1 = cards[0:16]
        hand2 = cards[16:32]
        hand3 = cards[32:48]
        hand4 = cards[48:64]
        await sio.emit('hand1', hand1)
        await sio.emit('hand2', hand2)
        await sio.emit('hand3', hand3)
        await sio.emit('hand4', hand4)
    elif playerCount == 5:
        hand1 = cards[0:13]
        hand2 = cards[13:26]
        hand3 = cards[26:39]
        hand4 = cards[39:52]
        hand5 = cards[52:64]
        await sio.emit('hand1', hand1)
        await sio.emit('hand2', hand2)
        await sio.emit('hand3', hand3)
        await sio.emit('hand4', hand4)
        await sio.emit('hand5', hand5)
    elif playerCount == 6:
        hand1 = cards[0:11]
        hand2 = cards[11:22]
        hand3 = cards[22:33]
        hand4 = cards[33:44]
        hand5 = cards[44:54]
        hand6 = cards[54:64]
        await sio.emit('hand1', hand1)
        await sio.emit('hand2', hand2)
        await sio.emit('hand3', hand3)
        await sio.emit('hand4', hand4)
        await sio.emit('hand5', hand5)
        await sio.emit('hand6', hand6)
    else: 
        hand1 = ['litty committee']
    await sio.emit('hideInit', playerCount)

@sio.on('hideRoom1')
async def hideRoom1(sid):
    await sio.emit('hideRoom1')

@sio.on('roomInit1')
def begin_chat(sid):
    sio.enter_room(sid, 'room1')

@sio.on('showHand1')
async def showHand1(sid):
    await sio.emit('hand1Reveal', room='room1')

@sio.on('hideRoom2')
async def hideRoom2(sid):
    await sio.emit('hideRoom2')

@sio.on('roomInit2')
def begin_chat(sid):
    sio.enter_room(sid, 'room2')

@sio.on('showHand2')
async def showHand2(sid):
    await sio.emit('hand2Reveal', room='room2')

@sio.on('hideRoom3')
async def hideRoom3(sid):
    await sio.emit('hideRoom3')

@sio.on('roomInit3')
def begin_chat(sid):
    sio.enter_room(sid, 'room3')

@sio.on('showHand3')
async def showHand3(sid):
    await sio.emit('hand3Reveal', room='room3')

@sio.on('hideRoom4')
async def hideRoom4(sid):
    await sio.emit('hideRoom4')

@sio.on('roomInit4')
def begin_chat(sid):
    sio.enter_room(sid, 'room4')

@sio.on('showHand4')
async def showHand4(sid):
    await sio.emit('hand4Reveal', room='room4')

@sio.on('hideRoom5')
async def hideRoom5(sid):
    await sio.emit('hideRoom5')

@sio.on('roomInit5')
def begin_chat(sid):
    sio.enter_room(sid, 'room5')

@sio.on('showHand5')
async def showHand5(sid):
    await sio.emit('hand5Reveal', room='room5')

@sio.on('hideRoom6')
async def hideRoom6(sid):
    await sio.emit('hideRoom6')

@sio.on('roomInit6')
def begin_chat(sid):
    sio.enter_room(sid, 'room6')

@sio.on('showHand6')
async def showHand6(sid):
    await sio.emit('hand6Reveal', room='room6')

@sio.on('playedCard')
async def playedCard(sid, playedCard):
    await sio.emit('playedCard', playedCard)

@sio.on('sendCard1')
async def playedCard(sid, sendCard1):
    await sio.emit('sendCard1', sendCard1)

@sio.on('sendCard2')
async def playedCard(sid, sendCard2):
    await sio.emit('sendCard2', sendCard2)

@sio.on('sendCard3')
async def playedCard(sid, sendCard3):
    await sio.emit('sendCard3', sendCard3)

@sio.on('sendCard4')
async def playedCard(sid, sendCard4):
    await sio.emit('sendCard4', sendCard4)

@sio.on('sendCard5')
async def playedCard(sid, sendCard5):
    await sio.emit('sendCard5', sendCard5)

@sio.on('sendCard6')
async def playedCard(sid, sendCard6):
    await sio.emit('sendCard6', sendCard6)

@sio.on('message')
async def my_message(sid):
    await sio.emit('greeting', 'Welcome!', room='room1')

# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)