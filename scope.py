global global_sound
global_sound = "HELLO"

def speak(animal_sound):
    global global_sound
    print "animal_sound: " + animal_sound
    print "global_sound: " + global_sound
    local_sound = "Hi there"
    print "local_sound: " + local_sound
    animal_sound = "bye"
    global_sound = "HARK"
    print "animal_sound: " + animal_sound

print "global_sound: " + global_sound
speak("Bark")
print "global_sound: " + global_sound
print "local_sound: " + local_sound
