# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'Agroco',
    'version': '12.0e.0.0.0',
    'license': 'AGPL-3',
    'category': 'Tools',
    'summary': 'Customization para Agrocolombia',
    'author': 'jeo Software',
    'depends': [

        # localizacion colombiana
        'l10n_co',         # Colombia - Contabilidad
        'l10n_co_edi',     # Electronic invoicing for Colombia with Carvajal
        'l10n_co_reports'  # Colombia - informes contables

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-agroco', 'branch': '12.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '12.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '10.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
    ],
}
