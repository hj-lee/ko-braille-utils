# This was 'Unicode Hangul Jamo utility.'
# Modified for this project.

# Below is orignal license block

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Hunspell Korean spellchecking dictionary.
#
# The Initial Developer of the Original Code is
# Changwoo Ryu.
# Portions created by the Initial Developer are Copyright (C) 2009
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): See CREDITS file
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

def define_unicode_vars(dic, start, end, unicodeprefix, prefix):
    import unicodedata
    for code in range(start, end + 1):
        char = chr(code)
        unicodename = unicodedata.name(char)
        if not unicodename.startswith(unicodeprefix):
            raise "Code name mismatch"
        name = prefix + unicodename[len(unicodeprefix):].replace('-', '_')
        dic[name] = char

_L_START = 0x1100
_L_END = 0x1112
_V_START = 0x1161
_V_END = 0x1175
_T_START = 0x11a8
_T_END = 0x11c2

def _define_jamo(start, end, unicodeprefix, prefix):
    define_unicode_vars(globals(), start, end, unicodeprefix, prefix)        
        
_define_jamo(_L_START, _L_END, 'HANGUL CHOSEONG ', 'L_')
_define_jamo(_V_START, _V_END, 'HANGUL JUNGSEONG ', 'V_')
_define_jamo(_T_START, _T_END, 'HANGUL JONGSEONG ', 'T_')
