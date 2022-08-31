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
#It must be defined before it is called, so the PushButton code will come next. 
def light_on():
    led.toggle()
    if led.is_lit:
        button_light.text = "Turn LED off!"
    else:
        button_light.text = "Turn LED on!"
    


#normally you have to call a function by itself for it to work,
#but in guizero you can comman a PushButton with a function.
#In the next line, I call the light_on function in the code 
#that creates the PushButton on my GUI.  

button_light = PushButton(app, command = light_on, text = "Click me to turn on the light!")

#This is the function that calls the GUI "into existence" 
app.display()