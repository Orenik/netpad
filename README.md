# Introduction - what is NetPad?
instead of drafting in multiple instances of notepad or an ide, consider netpad --
share text between devices over local network (single page webapp / server), with multiple textboxes.

# install options
- download built version (windows x64)
- download source and run inside ide
- download source and build executable

# build
1. download source and open in ide such as pycharm
   
2. in the terminal run the following command to build an executable:
   
   pyinstaller --onefile --clean --add-data "templates;templates" -i netpad.ico main.py
   
   you may need to install the following dependencies:
   * pip install flask
   * pip install pyinstaller

# usage
- running the app starts an http server listening at localhost:5000
- navigate to this address to access the NetPad client from any device on the local network.
- (if you are not using the host device to access the client, use an explicit ip address as localhost won't refer to the correct machine)
- use Save All button to save textbox contents onto the hosting machine.

thanks for using, please credit if redistributed or modified <3
