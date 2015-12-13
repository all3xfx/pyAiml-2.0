#        pyAiml-2.0 Python portring for AIML 2.0 implementation
#        Contact: cosimo.iaia@gmail.com
#
#       This library is free software; you can redistribute it and/or
#        modify it under the terms of the GNU Library General Public
#        License as published by the Free Software Foundation; either
#        version 2 of the License, or (at your option) any later version.
#
#        This library is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#        Library General Public License for more details.
#
#        You should have received a copy of the GNU Library General Public
#        License along with this library; if not, write to the
#        Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
#        Boston, MA  02110-1301, USA.
#
#

class Nodemapper:
	
	def __init__(self):
		self.category = None;
		self.height = MagicNumbers.max_graph_height;
		self.starBindings = None;
		self.map = None;	# {Str: NodeMapper}
		self.key = ''
		self.value = None	# Nodemapper
		self.shortCut = False
		self.sets = []
		
