from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json
from sense_hat import SenseHat
sense=SenseHat()
colors = [[10, 10, 10] for i in range(64)]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

# Converts a RGB color expressed in HEX to RGB. HEX comes
# from the server, and RGB array used by SenseHAT.
def hex_to_rgb_color(color: str):
    color = color.strip('#')
    rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    return rgb

# Button ids on html are integers.
# This function maps the led index to x and y.
def map_index_to_xy(led_index: int):
    return int(led_index % 8), int(led_index / 8)

@app.route('/')
def index():
    return render_template('Lab3-Colour-Picker.html')

# When users connect to the server using a webbrowser, a websocket is opened
# and this function is called to send the current LED colors
@socketio.on('connect')
def send_led_colors():
    print(f"sending colors.. {json.dumps(dict(colors=colors))}")
    emit('current_colors', json.dumps(dict(colors=colors)))

# When user clicks on a <div> in the webpage, the javascript sends a
# message encoded as update_led, where data contains the id of the <div>
# and the color of set in the <colorpicker>.
# Once the color is set, the server sends a broadcast message to all
# connected clients, which updates the LED color at each webbrowser screen.
@socketio.on('update_led')
def update_led_color(data):
    data = json.loads(data)
    x, _ = map_index_to_xy(int(data['id']))
   
    # Ignore updates for even-numbered columns (0,2,4,...)
    if x % 2 == 0:
        return  # Do nothing and do not emit any update to the web

    color_rgb = hex_to_rgb_color(data['color'])
    colors[int(data['id'])] = color_rgb
    sense.set_pixels(colors)
   
    # Only emit the update if it was applied
    emit('update_led',
         json.dumps(dict(
            id=data['id'],
            color=data['color'])),
         broadcast=True)


# New function to clear the LEDs when the button is pressed
@socketio.on('clear_leds')
def clear_leds():
    # Reset all colors to black
    global colors
    for i in range(64):
        colors[i]= [10, 10, 10] # Reset to initial state (or black)
        
    send_led_colors()
    sense.clear()
    # Emit the cleared colors to all connected clients
    emit('current_colors', json.dumps(dict(colors=colors)), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
