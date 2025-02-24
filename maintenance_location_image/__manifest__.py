# Copyright 2021 Exo Software
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Maintenance Location Image",
    "summary": """Adds images to Location.""",
    "category": "Manufacturing/Maintenance",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "zrtzrt",
    "maintainers": ["zrtzrt"],
    "website": "https://github.com/OCA/maintenance",
    "depends": ["maintenance_location"],
    "data": [
        "views/maintenance_location_views.xml",
    ],
    "installable": True,
    "application": False,
}
