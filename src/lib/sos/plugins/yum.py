### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools
import os

class yum(sos.plugintools.PluginBase):
    """yum information
    """

    optionList = [("yumlist", "list repositories and packages", "slow", False)]

    def checkenabled(self):
        if self.cInfo["policy"].pkgByName("yum") or os.path.exists("/etc/yum.conf"):
            return True
        return False

    def setup(self):
        # Pull all yum related information
        self.addCopySpec("/etc/yum")
        self.addCopySpec("/etc/yum.repos.d")
        self.addCopySpec("/etc/yum.conf")
        self.addCopySpec("/var/log/yum.log")

        if self.isOptionEnabled("yumlist"):
            # Get a list of channels the machine is subscribed to.
            self.collectExtOutput("/bin/echo \"repo list\" | /usr/bin/yum shell")
            # List various information about available packages
            self.collectExtOutput("/usr/bin/yum list")
      
        return
