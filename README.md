# Webex Space Archiver 

***Because of a 'refocus' this repository will no longer be maintained by myself.***  *Many thanks to the kinds words received from the users and the feedback they have been providing over the past years!*

Important Release v30!** (check out new features in the [release notes](#releasenotes))

[Features](#features)

[Start](#start)

[Configure](#configuration)

[Release notes](#releasenotes)

[Troubleshooting](#troubleshooting)

[Feedback & Support](#feedback)



# REQUIREMENTS
* A (free) [Webex](https://www.webex.com/team-collaboration.html) account
* Python 3.9 or higher (not tested with 3.6)
* Python '[requests](http://docs.python-requests.org/en/master/user/install/#install)' library
* Be a member of the Webex message space you want to archive
* Mac: SSL fix (see [troubleshooting](#troubleshooting) section at the end)  


<a name="features"/>
        

## NOTE:

* The message TIME **displayed** is in the UTC timezone. The timezone on your device defines how this UTC time/date is displayed. A message send at 12:43 CEST is stored as 10:43 UTC. When you change your timezone to PDT (UTC-7) it will be displayed as 03:43.
* When **printing** the generated HTML file in Firefox: File, Print, check "print background colors and images", then print or save to PDF
* To store your Webex token in an environment variable:
  * Windows: ```set WEBEX_ARCHIVE_TOKEN=YOUR_TOKEN_HERE```
  * Mac: ```export WEBEX_ARCHIVE_TOKEN='YOUR_TOKEN_HERE'```


<a name="start"/>

# Start

1. Meet the requirements

2. Run the script (```python webex-space-archive.py```) to _create the configuration file_ "webexspacearchive-config.ini" (if it does not exist)

3. In the webexspacearchive-config.ini file, save your developer token or (👍better!) create an environment variable called "WEBEX_ARCHIVE_TOKEN" with your token 

4. Run the script: ```python webex-space-archive.py```

| parameter |  |
| ------------- | ------------- |
| *nothing* | use standard configuration .ini file |
| CONFIG_FILE | use non-standard configuration .ini file<br>```testspace.ini``` |
| SEARCH_STRING | search for space name to get the space ID<br>```ciscolive``` |
| SPACE_ID | use this SPACE_ID with standard configuration .ini file<br>```Y2lzY29zcGFyazovL3VzL0lfS05FVy95b3Vfd291bGRfdHJ5X2hhaGE``` |
| CONFIG_FILE SPACE_ID | use non-standard configuration .ini file _and_ provided SPACE_ID<br>```a combination of examples above``` |
| SPACE_ID CONFIG_FILE | use non-standard configuration .ini file _and_ provided SPACE_ID |



**UPGRADE?**
Replace the .py file and keep the configuration file (.ini). 
To get changes in the .ini file, run the script once without .ini file and it will create one for you with the latest remarks and features.


<a name="configuration"/>

# Configuration
Edit the following variables in the python file:

---

**Personal Token**: you can find this on [developer.webex.com](https://developer.webex.com/docs/api/getting-started), login (top right of the page) and then scroll down to "Your Personal Access Token".
_NOTE_ see the 'NOTE' section above to see how you can also use an environment variable to store your token!
> **mytoken = "YOUR_TOKEN_HERE"**

***NOTE***: This token is valid for 12 hours! Then you have to get a new Personal Access Token.

---

**Space ID**: To find this, first save your developer token in the .ini file. Then run the script with a search arguments as a parameter. It will list all spaces+spaceId that match you search argument.
Alternatively: go to [Webex Developer List rooms](https://developer.webex.com/docs/api/v1/rooms/list-rooms), make sure you're logged in, set the 'max' parameter to '900' and click Run.
If you don't see the RUN button, make sure 'test mode' is turned on (top of page, under "Documentation")
TIP: to get the space ID of a space that you are in, in the client go to help / copy space details. Then in Webex talk to the bot "spaceidbot@webex.bot" and paste the space details. In return you get the space ID to be used here
> **myspaceid = "YOUR_SPACE_ID_HERE"**


---

**Downloadfiles**: do you want to download images or images & files? Think about it. Downloading images *and* files can significantly increase the archive time and consume disk space.  Downloaded images or files are stored in the subfolder. Options:
> **downloadfiles = info**

- "no"         : (default) no downloads, only show the text "file attachment"
- "info"       : no downloads, only show the filename and size
- "images"     : download images only
- "files"      : download files *and* images

---

**UserAvatar**: Do you want to show the user avatar or an icon? Avatars are not downloaded but *linked*. That means the script will get the user Avatar URL and use that in the HTML file. So the images are not downloaded to your hard-drive. Needs an internet connection in order to display the Avatar images.
> **useravatar = link**

- "no"        : (default) show user initials
- "link"      : link to avatar images (needs internet connection!)
- "download"  : download avatar images

---

**Max Messages**: Restrict the number of messages that are archived.  Some spaces contain 100,000 messages and you may not want to archive all of them. To archive the *last* 5000 messages:
> **maxtotalmessages = 5000**

- (empty)     : (default) last 1,000 messages
- 4000        : (example) download the last 4,000 messages
- 60d         : (example) download messages from the last 60 days. 120d = 120 days
- 22052021-   : (example) download messages after May 22nd 2021 (ddmmyyyy-) *****
- 22052021-18082021: download messages between May 22nd and August 18 2021 (ddmmyyyy-ddmmyyyy) *****
* = date format configurable in the .py code, variable 'maxmsg_format'


---

**OutputFilename**: Enter the file name of the output HTML file. If EMPTY the filename will be the same as the Archived Space name (recommended).
> **outputfilename = yourfilename.html**

---

**Sorting**: of archived messages.
> **sortoldnew = yes**

- "yes"   : (default) last message at the bottom (like in the Webex client)
- "no"     : latest message at the top

---

**OutputJSON**: Besides the .html file, how would you like to store your messages?
> **outputjson = no**

- "no"        :(default) only generate .html file
- "yes/both"  :output message data as .json and .txt file
- "json"      :output message data as .json file
- "txt"       :output message data as .txt file


---

**DST**: Besides the .html file, how would you like to store your messages? Both EU and US examples are shown in the .ini file.
> **dst_start = L,7,3** (last Sunday of March)

> **dst_stop = L,7,10** (last Sunday of October)

- empty        :(default) using DST data from your (local) system
- parameter 1  : Week number in a month. 1-4 (1st, 2nd, 3rd, 4th) or L (last)
- parameter 2  : Weekday number. 1-7 (1=Monday, 7=Sunday) 
- parameter 3  : Month. 1-12 (1=January, 12=December)


---

**Blurring**: Blur names and email addresses in html file
> **blurring = yes**
- empty        :(default) no blurring
- "yes"  : Note that it is a *VISUAL* blur. Data can still be copy/pasted



<a name="troubleshooting"></a>

# Troubleshooting
Most of the errors should be handles by the script.
* **SSL Issue**: On a Mac: the default SSL is outdated & unsupported. Check out the *readme.rtf* in your Python Application folder. That folder also contains a "Install certificates.command" which should do the work for you.


<a name="releasenotes"></a>

# Release Notes

For old releasenotes click [here](https://github.com/DJF3/Webex-Message-space-archiver/blob/master/README-oldreleasenotes.md)

## Enhancements in release v30 - March 19th 2023

Overall: increased output quality and precision. Support for DST, privacy blurring, bulk processing

**Important Enhancements** - all based on user requests
- NEW: DST dates: support for MANUAL DST date configuration (in .ini file)
- NEW: DST dates: support for AUTOMATIC (local) DST recognition, displaying message timestamps correctly for summer and winter.
- NEW: DST dates: added ability to use "L" for "Last" (Sunday) (in situations with 5 sundays in a month, like March 2019)
- NEW: Blurring: option to (OPTICALLY!) blur email addresses & @mentions in msg content and statistics. 
           Text file output email addresses replaced with "___@__.__". NOTE: JSON output will remain original
           NOTE: if you print the HTML file to PDF, the blurred data turns into images --> unable to get the original names
- NEW: Batch processing: call script with spaceId or spaceId+.ini file 

**IMPROVEMENTS**
- CONFIG: On "token problem" - mention environment variable "WEBEX_ARCHIVE_TOKEN"
- CONFIG: ini config: 'file download' section allow for the word "image" and "file" (besides "imageS" and "fileS")
- VISUAL: added collaps/expand-all button for months in the header
- VISUAL: added 'outputjson' and 'dst' settings to the HTML header
- VISUAL: HTML header "between 70 and 150 days" --> "between 70-150 days"
- VISUAL: Textfile output: extra line-break after <File Attachment>
- VISUAL: DST HTML header: TZ field shows the current TZ name, not both DST and non-DST name

**FIXED**
- VISUAL: move @mention css to .atmention class (so it can be included in blurs)
- VISUAL: TEXT output: no space between the email address and the message text
- VISUAL: HTML header shows "Generate HTML code for 12828 messages" = total count BEFORE limiting by date/days. 
- TEXT output: if msg only has an attachment and NO text or html the script crashes
- TEXT output: if msg has no text field, no return was added in the txt output
- TEXT output: now using the "text" field as the basis, not the converted "html" field
- TEXT output: DST date/time written to TXT file was UTC --> now local timezone OR with DST if configured
- CONFIG: change dst setting explanation "position" to "week-in-month"
- CONFIG: text generated in ini file was lowercased. Fixed.
- FIX: msg with html field but without text showed error on screen --> moved to the end, printing html text
- FIX: A single thread reply outside the original date-scope should not generate a TOC entry. (causing slightly less accurate msg count)
- FIX: missing_parent_msg["text"] has html tags which don't render in the 'text' field. Changed to 'html'
- FIX: Restrict messages between 2 dates failed. Fixed date check.
- FIX: DST in Australia: dst_start date is in the FALL and dst_stop in spring - now working correctly
- FIX: DST Utcoffset calculation was wrong for negative UTC offset timezones. fixed.

**NOTE**
- CARDS: cards and buttons won't be visible in the html output

# Info
- [DST dates](https://www.timeanddate.com/time/dst/2023.html) around the world


<a name="feedback"/>

# Feedback & Support
[Submit here](https://tools.sparkintegration.club/forms/joinspace/nwyadwh6l3oye5ikqhkfyzh73abwjf), open an issue or if you know my email address: send a message on Webex (not via email!).
