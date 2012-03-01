= NVDA snapshotVersionChecker =

Version: 1.2
Date: 2012-03-01
Author: Rui Batista
Contact: ruiandrebatista@gmail.com


This NVDA plugin reports if there is a more recent  NVDA snapshot available prompting the user to download it. Because there may be many branches the plugin reports information about the branch of the currently running snapshot version.

== How to Use? ==

Copy the snapshotVersionChecker folder to the globalPlugins folder of your NVDA installation. 
If you are running a installer version of NVDA please copy the folder to your user plugins directory at %APPDATA%\nvda\globalPlugins.

== Important note ==

This plugin *only* works with NVDA snapshot versions. It is intended for that purpose exclusively. This is a convenience, not a feature that one would not live without.

== Translations ==

The Plugin is translatable with the gettext framework. If you want to translate it please get in touch to

Rui Batista <ruiandrebatista@gmail.com>

== ChangeLog ==

Version 1.2
* Using custom webservice to retrieve information.
* Spanish translation.

Version 1.1:
* The plugin redirects the user to the snapshot download link instead of the snapshots webpage. Type of snapshot (installer or porttable) is deduced according to the currently running copy
* Disable the plugin on secure instances of NVDA (i.g. login and secure desktops).

Version 1.0:
* Initial Release.

== Contributors ==

Nicolás Garay Tapia <mk360@ug.uchile.cl>
* Spanish Translation.
