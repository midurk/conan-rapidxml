#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class RapiXMLConan(ConanFile):
    name = "rapidxml"
    version = "1.13"
    description = "RapidXml is an attempt to create the fastest XML parser possible"
    url = "https://github.com/bincrafters/conan-rapidxml"
    homepage = "http://rapidxml.sourceforge.net"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = ("BSL-1.0", "MIT")
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "name_lookup_changes_fix.patch"]
    source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        source_url = "https://cfhcable.dl.sourceforge.net/project/rapidxml/rapidxml/rapidxml%20"
        tools.get("{0}{1}/{2}-{3}.zip".format(source_url, self.version, self.name, self.version))
        os.rename(self.name + "-" + self.version, self.source_subfolder)
        tools.patch(base_path=self.source_subfolder, patch_file="name_lookup_changes_fix.patch")

    def package(self):
        self.copy(pattern="license.txt", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src=self.source_subfolder)

    def package_id(self):
        self.info.header_only()
