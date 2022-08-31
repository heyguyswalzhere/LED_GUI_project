from guizero import App, Text, PushButton
from gpiozero import LED, Button
from signal import pause

app = App(title ="Shed some light on the issue...")


#this greets the user
welcome_message = Text(app, text = "Press the button to turn on a light!", size = 12, font = "Courier", color = "red")


#this assigns the LED code from gpiozero to a variable named led
#the 17 refers to the gpio pin. We don't want to use the 3.3 or the 3.5 power pin
#We want the program to control when the pin gets power
led = LED(17)


#This is the function that controls the light
def light_on():
    led.toggle()
    if led.is_lit:
        button_light.text = "Turn LED off!"
    else:
        button_light.text = "Turn LED on!"
    


    

button_light = PushButton(app, command = light_on, text = "Click me to turn on the light!")

    
app.display()