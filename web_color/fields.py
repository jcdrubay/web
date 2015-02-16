# -*- encoding: utf-8 -*-
############################################################################
#
# OpenERP, Open Source Web Color
# Copyright (C) 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# Copyright (C) 2014 Anybox <http://anybox.fr>
# Copyright (C) 2015 Taktik SA <http://taktik.be>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# @author Étienne Beaudry Auger <etienne.b.auger@savoirfairelinux.com>
# @author Adil Houmadi <ah@taktik.be>
#
##############################################################################
from openerp import fields
from openerp.osv import fields as fields_osv


class Color(fields.Char):
    type = 'color'

    def __init__(self, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.size = 7


fields.Color = Color


class color(fields_osv.char):
    _type = 'color'

    def __init__(self, *args, **kwargs):
        kwargs['size'] = 7
        super(color, self).__init__(*args, **kwargs)


fields_osv.color = color