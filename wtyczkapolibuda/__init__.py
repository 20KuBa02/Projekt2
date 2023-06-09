# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaNaZajeciah
                                 A QGIS plugin
 wtyczka do Qgis
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-22
        copyright            : (C) 2023 by Jakub Tokarski
        email                : 01169935@pw.edu.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WtyczkaNaZajeciah class from file WtyczkaNaZajeciah.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .WtyczkaPolibuda import WtyczkaNaZajeciah
    return WtyczkaNaZajeciah(iface)
