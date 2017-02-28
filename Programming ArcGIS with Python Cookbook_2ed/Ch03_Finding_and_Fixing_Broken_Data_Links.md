
# Chapter 3: Finding and Fixing Broken Data Links

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 3: Finding and Fixing Broken Data Links](#chapter-3-finding-and-fixing-broken-data-links)
  * [3.1 Introduction](#31-introduction)
  * [3.2 Finding broken data sources in your map document and layer files](#32-finding-broken-data-sources-in-your-map-document-and-layer-files)
  * [3.3 Fixing broken data sources with MapDocument](#33-fixing-broken-data-sources-with-mapdocument)
  * [3.4 findAndReplaceWorkspacePaths()](#34-findandreplaceworkspacepaths)
  * [3.5 Fixing broken data sources with MapDocument.replaceWorkspaces()](#35-fixing-broken-data-sources-with-mapdocumentreplaceworkspaces)
  * [3.6 Fixing individual layer and table objects with replaceDataSource()](#36-fixing-individual-layer-and-table-objects-with-replacedatasource)
  * [3.7 Finding broken data sources in all map documents in a folder](#37-finding-broken-data-sources-in-all-map-documents-in-a-folder)

<!-- tocstop -->

In this chapter, we will cover the following recipes:
* Finding broken data sources in your map document and layer fies
* Fixing broken data sources with MapDocument.fidAndReplaceWorkspacePaths()
* Fixing broken data sources with MapDocument.replaceWorkspaces()
* Fixing individual layer and table objects with replaceDataSource()
* Finding broken data sources in all map documents in a folder

## 3.1 Introduction

It is not uncommon for your GIS data sources to move, migrate to a new data format, or be deleted.
The result can be broken data sources in many map documents or layer files.
These broken data sources can't be used until they're fixed, which can be an overwhelming process if the same changes need to be made across numerous map documents.
You can automate the process of finding and fixing these data sources using arcpy.mapping, without ever having to open the affected map documents.
Finding broken data sources is a simple process requiring the use of the ListBrokenDataSources() function, which returns a Python list of all broken data sources in a map document or layer file.
Typically, this function is used as the first step in a script that iterates through the list and fixes the data source.
Fixing broken data sources can be made in an individual data layer or across all layers in a common workspace.



## 3.2 Finding broken data sources in your map document and layer files

## 3.3 Fixing broken data sources with MapDocument

## 3.4 findAndReplaceWorkspacePaths()

## 3.5 Fixing broken data sources with MapDocument.replaceWorkspaces()

## 3.6 Fixing individual layer and table objects with replaceDataSource()

## 3.7 Finding broken data sources in all map documents in a folder
