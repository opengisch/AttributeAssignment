# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeAssignment
                                 A QGIS plugin
 Easy to assign an attribute on QGIS
                              -------------------
        begin                : 2017-09-18
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Yasunori Kirimoto
        email                : contact@day-journal.com
        license              : GNU General Public License v2.0
 ***************************************************************************/
"""

def classFactory(iface):
    from .AttributeAssignment import AttributeAssignment
    return AttributeAssignment(iface)
