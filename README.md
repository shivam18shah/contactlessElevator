# contactlessElevator v1

How to set up RaspberryPi

    Programming Raspbian Os on SD card

        Insert the microSD card in the card reader
        Setting the SD card in your Raspberry Pi: https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2
    
    
    Setting the Raspberry Pi for use
        
        Using GUI, monitor, keyboard and mouse
            Insert the microSD card in the card slot
            Connect the micro HDMI the the monitor slot near the power (left) and the other HDMI end to a monitor
            Connect the USB cable of wire and mouse (or bluetooth dongle for wireless) to the USB slots shown as Keyboard and Mouse
            Connect type C power cable (5V 3A or 5V 1A rating) to the power connector
            Turn the power on and the RaspberryPi is ready to be used
            For internet access, connect the Pi to Wifi or insert a LAN cable in Network slot
            

Details of all the prototype scripts

    a directory labeled model which contains the AI models for speech to text algorithm which the VOSK library uses. 
        Do Not rename or delete this folder, will render the project useless.
    controlLib.py which is a collection of classes and functions used to generate control signals to the first and second floor buttons
    micStreaming.py which is a collection of classes and functions to capture the audio stream, convert it to text and use the controlLib functions to generate the control signals.
    wrapperScript.sh which is a shell script to keep the python script running in case of some fault or expedition killing the python process.
        If the RaspberryPi shutdown, the shell script will also shutdown.
    If you want the wrapperScript to start auto-running on powerup, explore this option. Google has many tutorials on how to do this.
    


Installing dependencies and codes for prototype
    
    Raspbian OS is a linux based operating system and supports most of the Linux commands on it. Start the terminal on RaspberryPi, type one at a time and press enter to run. Below are the steps:
        sudo apt-get install python3-pip python3-dev
        git clone https://github.com/alphacep/vosk-api.git
        cd vosk-api/python
        python3 setup.py
        sudo pip3 install vosk
        pip3 install PyAudio
        cd ~ (Go back to home directory)
        gh repo clone shivam18shah/contactlessElevator (will get all the code files)
        (Other dependencies if missing will be printed on terminal while running the code and should be installed accordingly)
        

Setting up crontab jobs for script automation / Starting scripts without crontab
    Execute the following command in a terminal
        crontab -l : to check for any scheduled cron jobs
    Confirm that nothing has been scheduled yet
        crontab - e : then choose a text editor once it asks for it 
    In the editor tab type 5 * * * * source ~/finalCodes/wrapperScript.sh
    Note:
        there is a space after last asterisk and ./
        check any of the above links to check what is the format for the 5 asterisk which is min, hr, day of the month, month, day of the week
    Save and close the editor which will ensure that the wrapperScript runs every 5 min.
    
    Further research can be done to improve it, you can start the script by going to the finalCodes folder (type cd ~/finalCodes) and then type source wrapperScript.sh command in the terminal. Thus, following this step should start the code.
    Since the script will be running in the background, if you want to kill the script, then
        type ps aux in terminal
        look for the PID (it will be number) of micStreaming in the list printed
        type kill PID (replace PID with actual PID number of script) to stop the script
        To restart the script, again type the command above in bold.
    Please note that the links for reference materials are included at the end of this README
    

Final installation
    The final installation is to be done using the RaspberryPi installation kit screws. The following instructions should be taken:
        Holes can be drilled on the acrylic board in similar arrangement as above and then the components and be held in place using the installation kit screws.
        Remember to keep the pins of the component (4) in the diagram above facing upwards else, you won't be able to make the pin connections.
        Male to female or female to female connectors (included in the components ordered) can be used to make all the other  connections (except the one colored red in the circuit diagram) wherever required.
        Anything specific to the pinout diagram of individual diagrams eg (solid state relay - to understand which pin is which (total 4 pins on ssd)) can be found by Google search of the specific part.

    Common practices and suggestions:
        Check individual parts before making the final connection, check voltages using multimeter to check if the voltages and currents are in range and do not damage the components.
        You can type the command “pinout” (without double quotes) in the RaspberryPi terminal to get the pin diagram of RaspberryPi 4 GPIOs.
        Remember to turn off the Wifi connection of RaspberryPi after programming to avoid it getting tampered with. It is a requirement that RPi remains offline.
        Put a login and password to login to RaspberryPi (videos can be found on Google) to block random access to RaspberryPi.
        Do not pull the power USB from RPi unless you shutdown the RaspberryPi from GUI or using terminal command.
        
        
Starting the prototype after installation
    After the RaspberryPi has been connected to the elevator panel, it's time to start the crontab job to start the prototype.
    When you are downloading the codes on RaspberryPi, don't forget to turn on the SSH connection from the RaspberryPi config (Google how to).
    To do this,you can connect an ethernet cable from RaspberryPi to your laptop ethernet port.
    Open a command line application like MobaXterm or Putty and open its terminal.
    Type ssh raspberrypi.local (it's important that SSH has to be turned on on RPi)
    Type the password in and you will get access to the command line terminal of RPi where you can follow Step 4 in the tutorial and get the crontab job running
    This should ensure the prototype starts running.
    Test the prototype before and after closing the elevator panel.


Giving the voice commands:
    Trigger commands: Hey Elevator, Okay Elevator, Hi Elevator
    Floor Commands: First Floor, Second Floor


Useful references:
    Linux cron jobs: https://www.youtube.com/watch?v=QZJ1drMQz1A
    Cron jobs every 5 minutes: https://crontab.guru/every-5-minutes
    Periodic cron jobs: https://www.thegeekstuff.com/2011/07/cron-every-5-minutes/
    Using cron jobs to run scripts automatically: https://www.jessicayung.com/automate-running-a-script-using-crontab/
    Scheduling a python script or cron job: https://gavinwiener.medium.com/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e
    Raspberry Pi documentation: https://www.raspberrypi.org/documentation/remote-access/ssh/
    Raspberry Pi setup: https://learn.adafruit.com/raspberry-pi-computer-quick-start
    
